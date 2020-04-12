Demo of creating a Python/Tkinter app in a Snapcraft package.

Full code example: https://github.com/argosopentechnologies/snapcraft-tkinter

I'm having trouble getting a Python/Tkinter app to run in a snap container. The python3-tk package isn't included with python and can't be installed with pip. When python3-tk is added as a stage-package like this:


parts:
  snapcraft-tkinter:
    plugin: python
    python-version: python3
    source: .
    stage-packages:
      - python3-tk


and you attempt to run a python program that uses tkinter you get this error:


Traceback (most recent call last):
  File "/snap/snapcraft-tkinter/x1/bin/snapcraft-tkinter", line 5, in <module>
    app.main()
  File "/snap/snapcraft-tkinter/x1/lib/python3.6/site-packages/tkinter_demo/app.py", line 7, in main
    window = Tk()
  File "/snap/snapcraft-tkinter/x1/usr/lib/python3.6/tkinter/__init__.py", line 2023, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: Can't find a usable init.tcl in the following directories: 
    /usr/share/tcltk/tcl8.6 /snap/snapcraft-tkinter/x1/usr/lib/tcl8.6 /snap/snapcraft-tkinter/x1/lib/tcl8.6 /snap/snapcraft-tkinter/x1/usr/library /snap/snapcraft-tkinter/x1/library /snap/snapcraft-tkinter/x1/tcl8.6.8/library /snap/snapcraft-tkinter/tcl8.6.8/library



This probably means that Tcl wasn't installed properly.


This is because the tcl library ends up in the wrong place in the snap. You are able to set the TCL_Library environment variable like this:


apps:
  snapcraft-tkinter: 
    command: bin/snapcraft-tkinter
    environment:
      TCL_LIBRARY: "$SNAP/usr/share/tcltk/tcl8.6"


However the documentation says that using this variable is a "last resort" workaround: https://wiki.tcl-lang.org/page/TCL_LIBRARY . If you add the environment variable then you are able to create a window with tkinter like this:


window = Tk()
window.title("Snapcraft Tkinter Demo")
window.mainloop()

If you try to add any elements to the window like this:


my_scrolledtext = ScrolledText(window, width=10, height=10)
my_scrolledtext.grid(column=0, row=0)


you get "Segmentation fault (core dumped)". I'm not sure if this is something wrong with the python snapcraft plugin, The way you add python3-tk as a dependency, something with tkinter, or me doing something wrong? Any ideas/workarounds?




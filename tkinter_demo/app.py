#!/usr/bin/env python3

from tkinter import *
from tkinter.scrolledtext import ScrolledText

def main():
    window = Tk()
    window.title("Snapcraft Tkinter Demo")
    my_scrolledtext = ScrolledText(window, width=10, height=10)
    my_scrolledtext.grid(column=0, row=0)
    window.mainloop()


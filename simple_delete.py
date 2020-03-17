#!/usr/bin/env python3

import tkinter as tk


ROOT_WIN = tk.Tk()
ROOT_WIN.title("Clear text")

IMP_FIELD = tk.Entry(ROOT_WIN)
IMP_FIELD.grid(row=0, column=0)


def clear():
    """Clear text in widget"""
    IMP_FIELD.delete(0, "end")
    return

CLEAR_BUT = tk.Button(ROOT_WIN, text="Clear text", command=clear)
CLEAR_BUT.grid(row=0, column=1)


ROOT_WIN.mainloop()

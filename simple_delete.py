#!/usr/bin/env python3
"""Sum, substracion numbers"""

import tkinter as tk
import random


ROOT_WIN = tk.Tk()
ROOT_WIN.title("Clear text")

FIRST_NUM = random.randint(1, 10)
SECOND_NUM = random.randint(1, 10)
print("First num %d" % FIRST_NUM)
print("Second num %d" % SECOND_NUM)

NUM1 = tk.Label(ROOT_WIN, text=FIRST_NUM)
NUM1.grid(row=0, column=0, padx=10, pady=10)
PLUS = tk.Label(ROOT_WIN, text="+")
PLUS.grid(row=0, column=1, padx=10, pady=10)
NUM2 = tk.Label(ROOT_WIN, text=SECOND_NUM)
NUM2.grid(row=0, column=2, padx=10, pady=10)
EQUAL = tk.Label(ROOT_WIN, text="=")
EQUAL.grid(row=0, column=3, padx=10, pady=10)


IMP_FIELD = tk.Entry(ROOT_WIN)
IMP_FIELD.focus_set()
IMP_FIELD.grid(row=0, column=4)


def check():
    """Executed when check button pressed"""
    num = IMP_FIELD.get()
    if int(num) == FIRST_NUM+SECOND_NUM:
        IMP_FIELD.configure({"background": "green"})
        return True
    IMP_FIELD.configure({"background": "red"})
    IMP_FIELD.delete(0, "end")
    return False

CHECK_BUT = tk.Button(ROOT_WIN, text="ПРОВЕРИ", command=check)
CHECK_BUT.grid(row=0, column=5)


ROOT_WIN.mainloop()

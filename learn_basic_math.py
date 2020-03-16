#!/usr/bin/env python3
"""Summ, subtraction numbers"""

import tkinter as tk
import random

ROOT = tk.Tk()

NUM = random.randint(1, 10)
# Define numbers
NUM1 = tk.Label(ROOT, text=NUM)
NUM1.grid(row=0, column=0, padx=10, pady=10)
PLUS = tk.Label(ROOT, text="+")
PLUS.grid(row=0, column=1, padx=10, pady=10)
NUM2 = tk.Label(ROOT, text=NUM)
NUM2.grid(row=0, column=2, padx=10, pady=10)
EQUAL = tk.Label(ROOT, text="=")
EQUAL.grid(row=0, column=3, padx=10, pady=10)



# Define input fields
ENTRY_WIDGET = tk.Entry(ROOT, text="NUM")
ENTRY_WIDGET.grid(row=0, column=4, padx=10, pady=10)

def my_click():
    """Executed when check_button pressed"""
    return

CHECK_BUTTON = tk.Button(ROOT, text="ПРОВЕРИ", padx=70, pady=20, command=my_click)
CHECK_BUTTON.grid(row=0, column=5, padx=10, pady=10)

ROOT.mainloop()

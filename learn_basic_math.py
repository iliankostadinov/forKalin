#!/usr/bin/env python3
"""Sum, substracion numbers"""

import tkinter as tk
import random

class One_Line(object):
    ROOT_WIN = tk.Tk()
    ROOT_WIN.title("Задачи за Калин")

    def __init__(self, row_num=0):
        self.first_num = random.randint(1, 10)
        self.second_num = random.randint(1, 10)
        print("First num %d" % self.first_num)
        print("Second num %d" % self.second_num)
        self.num1 = tk.Label(One_Line.ROOT_WIN, text=self.first_num)
        self.num1.grid(row=row_num, column=0, padx=10, pady=10)
        self.plus = tk.Label(One_Line.ROOT_WIN, text="+")
        self.plus.grid(row=row_num, column=1, padx=10, pady=10)
        self.num2 = tk.Label(One_Line.ROOT_WIN, text=self.second_num)
        self.num2.grid(row=row_num, column=2, padx=10, pady=10)
        self.equal = tk.Label(One_Line.ROOT_WIN, text="=")
        self.equal.grid(row=row_num, column=3, padx=10, pady=10)
        self.imp_field = tk.Entry(One_Line.ROOT_WIN)
        self.imp_field.grid(row=row_num, column=4)



    def check(self):
        """Executed when check button pressed"""
        num = self.imp_field.get()
        if int(num) == self.first_num+self.second_num:
            self.imp_field.configure({"background": "green"})
            return True
        self.imp_field.configure({"background": "red"})
        self.imp_field.delete(0, "end")
        return False


first_line = One_Line(0)
CHECK_BUT = tk.Button(One_Line.ROOT_WIN, text="ПРОВЕРИ", command=first_line.check)
CHECK_BUT.grid(row=0, column=5)

second_line =One_Line(1)
CHECK_BUT = tk.Button(One_Line.ROOT_WIN, text="ПРОВЕРИ", command=second_line.check)
CHECK_BUT.grid(row=1, column=5)

One_Line.ROOT_WIN.mainloop()

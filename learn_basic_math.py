#!/usr/bin/env python3
"""Sum, substracion numbers"""

import tkinter as tk
import random


class OneLine():
    """Visualize one line for sum of two numbers"""

    def __init__(self, window, row_num=0):
        self.first_num = random.randint(1, 10)
        self.second_num = random.randint(1, 10)
        self.num1 = tk.Label(window, text=self.first_num, font=(600))
        self.num1.grid(row=row_num, column=0, padx=10, pady=10)
        self.plus = tk.Label(window, text="+")
        self.plus.grid(row=row_num, column=1, padx=10, pady=10)
        self.num2 = tk.Label(window, text=self.second_num, font=(600))
        self.num2.grid(row=row_num, column=2, padx=10, pady=10)
        self.equal = tk.Label(window, text="=", font=(600))
        self.equal.grid(row=row_num, column=3, padx=10, pady=10)
        self.imp_field = tk.Entry(window, font=(600))
        self.imp_field.grid(row=row_num, column=4)

    def check_sum(self):
        """Executed when check button pressed"""
        num = self.imp_field.get()
        if int(num) == self.first_num+self.second_num:
            self.imp_field.configure({"background": "green"})
            return True
        self.imp_field.configure({"background": "red"})
        self.imp_field.delete(0, "end")
        return False


class OneLineSubstr():
    """Visualize one line for substract two numbers """

    def __init__(self, window, row_num=0):
        self.first_num = random.randint(1, 20)
        self.second_num = random.randint(1, 20)
        if self.first_num < self.second_num:
            self.first_num, self.second_num = self.second_num, self.first_num
        self.num1 = tk.Label(window, text=self.first_num, font=(600))
        self.num1.grid(row=row_num, column=0, padx=10, pady=10)
        self.plus = tk.Label(window, text="--", font=("Arial", 13, "bold"))
        self.plus.grid(row=row_num, column=1, padx=10, pady=10)
        self.num2 = tk.Label(window, text=self.second_num, font=(600))
        self.num2.grid(row=row_num, column=2, padx=10, pady=10)
        self.equal = tk.Label(window, text="=", font=(600))
        self.equal.grid(row=row_num, column=3, padx=10, pady=10)
        self.imp_field = tk.Entry(window, font=(600))
        self.imp_field.grid(row=row_num, column=4)

    def check_substr(self):
        """Executed when check button pressed"""
        num = self.imp_field.get()
        if int(num) == self.first_num-self.second_num:
            self.imp_field.configure({"background": "green"})
            return True
        self.imp_field.configure({"background": "red"})
        self.imp_field.delete(0, "end")
        return False


class OneLineUnknown():
    """Visualize one line for find unknown number"""

    def __init__(self, window, row_num=0):
        self.first_num = random.randint(1, 20)
        self.second_num = random.randint(1, 20)
        if self.first_num > self.second_num:
            self.first_num, self.second_num = self.second_num, self.first_num
        self.num1 = tk.Label(window, text=self.first_num, font=(600))
        self.num1.grid(row=row_num, column=0, padx=10, pady=10)
        self.plus = tk.Label(window, text="+", font=("Arial", 13, "bold"))
        self.plus.grid(row=row_num, column=1, padx=10, pady=10)
        self.num2 = tk.Label(window, text=self.second_num, font=(600))
        self.num2.grid(row=row_num, column=4, padx=10, pady=10)
        self.equal = tk.Label(window, text="=", font=(600))
        self.equal.grid(row=row_num, column=3, padx=10, pady=10)
        self.imp_field = tk.Entry(window, font=(600))
        self.imp_field.grid(row=row_num, column=2)

    def check_unknown(self):
        """Executed when check button pressed"""
        num = self.imp_field.get()
        if int(num) == self.second_num-self.first_num:
            self.imp_field.configure({"background": "green"})
            return True
        self.imp_field.configure({"background": "red"})
        self.imp_field.delete(0, "end")
        return False

class OneLineUnknownMinus():
    """Visualize one line for find unknown number"""

    def __init__(self, window, row_num=0):
        self.first_num = random.randint(1, 20)
        self.second_num = random.randint(1, 20)
        if self.first_num < self.second_num:
            self.first_num, self.second_num = self.second_num, self.first_num
        self.num1 = tk.Label(window, text=self.first_num, font=(600))
        self.num1.grid(row=row_num, column=0, padx=10, pady=10)
        self.plus = tk.Label(window, text="--", font=("Arial", 13, "bold"))
        self.plus.grid(row=row_num, column=1, padx=10, pady=10)
        self.num2 = tk.Label(window, text=self.second_num, font=(600))
        self.num2.grid(row=row_num, column=4, padx=10, pady=10)
        self.equal = tk.Label(window, text="=", font=(600))
        self.equal.grid(row=row_num, column=3, padx=10, pady=10)
        self.imp_field = tk.Entry(window, font=(600))
        self.imp_field.grid(row=row_num, column=2)

    def check_unknown_minus(self):
        """Executed when check button pressed"""
        num = self.imp_field.get()
        if int(num) == self.first_num-self.second_num:
            self.imp_field.configure({"background": "green"})
            return True
        self.imp_field.configure({"background": "red"})
        self.imp_field.delete(0, "end")
        return False


if __name__ == "__main__":
    ALL_LINES = [("fir_line", 1), ("sec_line", 2), ("thrid_line", 3),
                 ("four_l", 4), ("five", 5), ("six", 6), ("sev", 7),
                 ("eight", 8), ("nine", 9), ("ten", 10)]
    ALL_LINES_COMB = [("fir_line", 1), ("sec_line", 2), ("thrid_line", 3),
                      ("four_l", 4), ("five", 5), ("six", 6), ("sev", 7),
                      ("eight", 8), ("nine", 9), ("ten", 10), ("ele", 11),
                      ("twelve", 12), ("thirteen", 13), ("fourteen", 14),
                      ("fifteen", 15), ("sixteen", 16)]

    root_win = tk.Tk()
    root_win.title("Задачи за Калин")
    root_win.geometry('1800x900')

    def summ_fun():
        """Creating name object for drawing summ examples"""
        for name, number in ALL_LINES:
            name = OneLine(root_win, number)
            check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                  command=name.check_sum)
            check_but.grid(row=number, column=5)

    def substr_fun():
        """Creating name object for drawing substrac examples"""
        for name, number in ALL_LINES:
            name = OneLineSubstr(root_win, number)
            check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                  command=name.check_substr)
            check_but.grid(row=number, column=5)

    def unknow_fun():
        """Creating name object for drawing unknown examples"""
        for name, number in ALL_LINES:
            name = OneLineUnknown(root_win, number)
            check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                  command=name.check_unknown)
            check_but.grid(row=number, column=5)

    def unknow_minus_fun():
        """Creating name object for drawing unknown examples"""
        for name, number in ALL_LINES:
            name = OneLineUnknownMinus(root_win, number)
            check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                  command=name.check_unknown_minus)
            check_but.grid(row=number, column=5)

    def combine_fun():
        """Create name object for drawing combine examples"""
        func_list = [OneLine, OneLineSubstr, OneLineUnknown, OneLineUnknownMinus]
        for name, number in ALL_LINES_COMB:
            func_name = random.choice(func_list)
            name = func_name(root_win, number)
            print(func_name)
            print(isinstance(func_name, OneLine))
            if func_name == OneLine:
                check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                      command=name.check_sum)
                check_but.grid(row=number, column=5)
            if func_name == OneLineSubstr:
                check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                      command=name.check_substr)
                check_but.grid(row=number, column=5)
            if func_name == OneLineUnknown:
                check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                      command=name.check_unknown)
                check_but.grid(row=number, column=5)
            if func_name == OneLineUnknownMinus:
                check_but = tk.Button(root_win, text="ПРОВЕРИ", font=(600),
                                      command=name.check_unknown_minus)
                check_but.grid(row=number, column=5)

    SUMM_BUT = tk.Button(root_win, text="СЪБИРАНЕ", font=(60),
                         command=summ_fun)
    SUMM_BUT.grid(row=0, column=1)
    SUBSTR_BUT = tk.Button(root_win, text="ИЗВАЖДАНЕ", font=(60),
                           command=substr_fun)
    SUBSTR_BUT.grid(row=0, column=2)
    UNKNOWN_BUT = tk.Button(root_win, text="НЕИЗВЕСТНО", font=(60),
                            command=unknow_fun)
    UNKNOWN_BUT.grid(row=0, column=3)
    COMB_BUT = tk.Button(root_win, text="КОМБИНИРАНИ", font=(60),
                         command=combine_fun)
    COMB_BUT.grid(row=0, column=4)
    UNKNOWN_MINUS_BUT = tk.Button(root_win, text="НЕИЗВЕСТНО С МИНУС",
                                  font=(60), command=unknow_minus_fun)
    UNKNOWN_MINUS_BUT.grid(row=0, column=5)

    root_win.mainloop()

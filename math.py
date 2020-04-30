#!/usr/bin/env python3

import tkinter as tk

HEIGHT = 700
WIDTH = 1000

root_win = tk.Tk()


#frame = tk.Frame(root_win)
#frame.place(relwidth=1, relheight=1)

button_summ = tk.Button(root_win, text="СЪБИРАНЕ", bg="grey")
button_summ.pack(side=tk.LEFT)
button_substr = tk.Button(root_win, text="ИЗВАЖДАНЕ", bg="grey")
button_substr.pack(side=tk.LEFT)

root_win.mainloop()

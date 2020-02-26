#! /usr/bin/env python3.7

import tkinter as tk

root = tk.Tk()
root.title("Neat (?)")


frame = tk.Frame(root)
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky="nsew")
grid = tk.Frame(frame)
grid.grid(sticky="nsew", column=0, row=7, columnspan=2)
tk.Grid.rowconfigure(frame, 7, weight=1)
tk.Grid.columnconfigure(frame, 0, weight=1)

# example values
for x in range(10):
    for y in range(5):
        btn = tk.Button(frame)
        btn.grid(column=x, row=y, sticky="nsew")

for x in range(10):
    tk.Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
    tk.Grid.rowconfigure(frame, y, weight=1)
root.mainloop()

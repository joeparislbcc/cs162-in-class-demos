#! /usr/bin/env python3.8
"""One-function calculator."""

import tkinter as tk


def do_action(arg):
    display.insert(tk.END, arg)


def compute():
    try:
        result = eval(display.get())
    except SyntaxError or NameError:
        clear()
        display.insert(0, "Invalid Expression!")
    else:
        clear()
        display.insert(0, result)


def clear():
    display.delete(0, tk.END)


root = tk.Tk()
root.title("One-function calculator")
root.geometry("250x350")
# root.configure(bg="floral white")

display = tk.Entry(root, borderwidth=5, text="")
display.grid(row=0, column=0, padx=10, pady=10, columnspan=4, sticky="we")
root.grid_columnconfigure((0, 1, 2, 3), uniform="equal", weight=1)
root.grid_rowconfigure((1, 2, 3, 4, 5), uniform="equal", weight=1)

button_7 = tk.Button(root, text="7", command=lambda: do_action("7")).grid(
    row=2, column=0, sticky="nsew"
)
button_8 = tk.Button(root, text="8", command=lambda: do_action("8")).grid(
    row=2, column=1, sticky="nsew"
)
button_9 = tk.Button(root, text="9", command=lambda: do_action("9")).grid(
    row=2, column=2, sticky="nsew"
)
button_4 = tk.Button(root, text="4", command=lambda: do_action("4")).grid(
    row=3, column=0, sticky="nsew"
)
button_5 = tk.Button(root, text="5", command=lambda: do_action("5")).grid(
    row=3, column=1, sticky="nsew"
)
button_6 = tk.Button(root, text="6", command=lambda: do_action("6")).grid(
    row=3, column=2, sticky="nsew"
)
button_1 = tk.Button(root, text="1", command=lambda: do_action("1")).grid(
    row=4, column=0, sticky="nsew"
)
button_2 = tk.Button(root, text="2", command=lambda: do_action("2")).grid(
    row=4, column=1, sticky="nsew"
)
button_3 = tk.Button(root, text="3", command=lambda: do_action("3")).grid(
    row=4, column=2, sticky="nsew"
)
button_0 = tk.Button(root, text="0", command=lambda: do_action("0")).grid(
    row=5, column=0, sticky="nsew"
)
button_dot = tk.Button(root, text=".", command=lambda: do_action(".")).grid(
    row=5, column=1, sticky="nsew"
)
button_divide = tk.Button(root, text=u"\u00F7", command=lambda: do_action("/")).grid(
    row=1, column=3, sticky="nsew"
)
button_multiply = tk.Button(root, text=u"\u00D7", command=lambda: do_action("*")).grid(
    row=2, column=3, sticky="nsew"
)
button_subtract = tk.Button(root, text=u"\u2212", command=lambda: do_action("-")).grid(
    row=3, column=3, sticky="nsew"
)
button_add = tk.Button(root, text=u"\u002B", command=lambda: do_action("+")).grid(
    row=4, column=3, sticky="nsew"
)
button_equals = tk.Button(root, text="=", bg="cornsilk2", command=compute).grid(
    row=5, column=2, columnspan=2, sticky="nsew"
)
button_left_paren = tk.Button(root, text="(", command=lambda: do_action("(")).grid(
    row=1, column=1, sticky="nsew"
)
button_right_paren = tk.Button(root, text=")", command=lambda: do_action(")")).grid(
    row=1, column=2, sticky="nsew"
)
button_clear = tk.Button(root, text="C", bg="azure", command=clear).grid(
    row=1, column=0, sticky="nsew"
)

root.mainloop()

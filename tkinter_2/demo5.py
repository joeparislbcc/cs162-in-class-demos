#! /usr/bin/env python3.7

import tkinter as tk

root = tk.Tk()

root.title("Window Geometry")

app_ico = tk.PhotoImage(file="images/white.png")
root.iconphoto(False, app_ico)

root.configure(padx=5, pady=5)
root.geometry("600x400+800+400")

exit_button = tk.Button(root, text="Exit", padx=10, pady=10, command=root.quit)
exit_button.pack()

root.mainloop()

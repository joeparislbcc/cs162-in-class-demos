#! /usr/bin/env python3.7

import tkinter as tk

root = tk.Tk()

root.title("Exit")

app_ico = tk.PhotoImage(file="images/white.png")
root.iconphoto(False, app_ico)
root.configure(width=600, height=400, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", padx=10, pady=10, command=root.quit)
exit_button.pack()

root.mainloop()

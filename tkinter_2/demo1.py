#! /usr/bin/env python3.7

import tkinter as tk

root = tk.Tk()

root.title("Setting the App Icon")

app_ico = tk.PhotoImage(file="images/white.png")
root.iconphoto(False, app_ico)

root.configure(width=600, height=400, padx=5, pady=5)

root.mainloop()

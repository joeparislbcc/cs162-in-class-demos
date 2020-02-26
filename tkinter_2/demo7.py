#! /usr/bin/env python3.7

import tkinter as tk
import requests
import json


def get_joke():
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    # print(res.status_code)
    # print(json.loads(res.text)["joke"])
    joke_text.set(json.loads(res.text)["joke"])


root = tk.Tk()

root.title("Front End")

app_ico = tk.PhotoImage(file="images/joke.png")
root.iconphoto(False, app_ico)

root.configure(bg="#dedede")
root.minsize(1024, 768)

tk.Grid.rowconfigure(root, (0), weight=1)
tk.Grid.rowconfigure(root, (1), weight=0)
tk.Grid.columnconfigure(root, (0), weight=1)

joke_text = tk.StringVar()

joke = tk.Label(
    root,
    font=("Comic Sans MS", 24, "italic"),
    text="placeholder text",
    textvariable=joke_text,
    anchor=tk.CENTER,
    justify=tk.CENTER,
    padx=20,
    pady=20,
    bg="#dedede",
    fg="#333",
    wraplength=500,
)
joke.grid()

controls = tk.Frame(root, padx=5, pady=10, bg="#ccc")
controls.grid(row=1, column=0, sticky="nsew")
# for k in controls.keys():
#     print(f"{k}: {controls[k]}")

joke_button = tk.Button(controls, text="Get Joke", command=get_joke)
joke_button.pack()
joke_button.focus()

root.mainloop()

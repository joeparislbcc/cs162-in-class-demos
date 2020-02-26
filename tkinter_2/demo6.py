#! /usr/bin/env python3.7

import tkinter as tk

HEIGHT = 600
WIDTH = 400

root = tk.Tk()

root.title("Centering the Window")

app_ico = tk.PhotoImage(file="images/white.png")
root.iconphoto(False, app_ico)

root.minsize(HEIGHT, WIDTH)
root.configure(padx=5, pady=5)

# get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"screen dimensions: {screen_width} x {screen_height}")

# compute the coordinate of the center of the screen
x_center = screen_width / 2
y_center = screen_height / 2
print(f"screen center: {x_center} x {y_center}")

# get the width and height of the window
root_width = HEIGHT
root_height = WIDTH
# root_width = root.winfo_width()
# root_height = root.winfo_height()
print(f"window dimensions: {root_width} x {root_height}")

# compute the offset needed to position the center of the window (rather than
# its top left corner) at the center of the screen
x_offset = root_width / 2
y_offset = root_height / 2
print(f"window offsets: {x_offset}, {y_offset}")

# compute the coordinate to place the top left corner of the window at in order
# to truly center it on the screen
x_coord = int(x_center - x_offset)
y_coord = int(y_center - y_offset)
print(f"window top left coordinate: {x_coord}, {y_coord}")

root.geometry(f"{root_width}x{root_height}+{x_coord}+{y_coord}")

exit_button = tk.Button(root, text="Exit", padx=10, pady=10, command=root.quit)
exit_button.pack()

root.mainloop()

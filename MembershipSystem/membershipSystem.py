# import libs
import tkinter as tk
from tkinter.constants import NW
from PIL import Image, ImageTk

root = tk.Tk()

# canvas (background)
canvas = tk.Canvas(root, width=1200, height=700)
canvas.grid(columnspan=5, rowspan=10)

# logo
logo = Image.open('MembershipSystem\logo-287x93.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)



### WIP ###




root.mainloop()
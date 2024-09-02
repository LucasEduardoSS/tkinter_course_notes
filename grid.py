# Positioning with TKinter's grid system
from tkinter import *

root = Tk()

# Creating Labels Widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Lucas")

# Shoving them into the screen
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()

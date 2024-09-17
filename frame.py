# Adding Frames to Your Program

from tkinter import *

# Header
root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('images/draw_snake32.ico')

# Main Frame
frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

# Buttons
b1 = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="Neither Here!")

# Buttons Grid
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)

root.mainloop()

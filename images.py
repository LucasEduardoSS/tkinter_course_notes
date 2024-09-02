# Using Icons, Images and Exit buttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Header
root.title('Using Images, Icons and Exit buttons')
root.iconbitmap('C:/Users/Lucas Eduardo/Downloads/draw_snake32.ico')

# Central Image
my_img = ImageTk.PhotoImage(Image.open("images/city.jpg"))
my_label = Label(image=my_img)
my_label.pack()

# Exit button
but_quit = Button(text="Exit Program", command=root.quit)
but_quit.pack()

root.mainloop()

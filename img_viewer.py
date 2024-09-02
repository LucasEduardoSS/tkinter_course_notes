# Build an Image Viewer App

from tkinter import *
from PIL import ImageTk, Image


def update(img_index):
    global next_img, prev_img, img_label
    # Update the image
    img_label["image"] = img_list[img_index]

    # Update the index variables
    next_img = img_index + 1
    prev_img = img_index - 1

    # Enable or disable navigation buttons
    if prev_img == -1:
        but_back["state"] = DISABLED
    elif next_img == len(img_list):
        but_next["state"] = DISABLED
    else:
        but_next["state"] = ACTIVE
        but_back["state"] = ACTIVE


root = Tk()

# Header
root.title('Image Viewer')
root.iconbitmap('C:/Users/Lucas Eduardo/PycharmProjects/TkinterCourse/images/draw_snake32.ico')

# Images
img1 = ImageTk.PhotoImage(Image.open("images/landscape1_720.png"))
img2 = ImageTk.PhotoImage(Image.open("images/landscape2_720.png"))
img3 = ImageTk.PhotoImage(Image.open("images/landscape3_720.jpg"))

img_list = [img1, img2, img3]

# Auxiliary Variables
start_img = 0
next_img = start_img + 1
prev_img = start_img - 1

# Image Label
img_label = Label(image=img_list[start_img])
img_label.grid(row=0, column=0, columnspan=3)

# Buttons
but_back = Button(root, text="<<", command=lambda: update(prev_img), state=DISABLED if start_img == 0 else ACTIVE)
but_next = Button(root, text=">>", command=lambda: update(next_img), state=DISABLED if start_img == len(img_list)-1 else ACTIVE)
but_exit = Button(root, text="Exit Program", command=root.quit)

# Display Buttons
but_back.grid(row=1, column=0)
but_next.grid(row=1, column=2)
but_exit.grid(row=1, column=1)

root.mainloop()

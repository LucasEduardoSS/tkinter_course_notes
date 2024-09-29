from tkinter import *

# Root
root = Tk()
root.title('Creating Radio Buttons')
root.iconbitmap('images/draw_snake32.ico')


def clicked(value):
    myLabel1["text"] = value
    myLabel1.pack()


# Variables
var = IntVar()
pizza = StringVar()

# Pizza flavors
flavors = [
    ("Pepperoni", "Pepperoni"),
    ("Calabresa", "Calabresa"),
    ("Portuguesa", "Portuguesa"),
    ("4 Queijos", "4 Queijos")
]

# Pizza flavor selection
for text, flavor in flavors:
    Radiobutton(root, text=text, variable=pizza, value=flavor).pack()

# Radiobutton(root, text="Option 1", variable=var, value=1, command=lambda : clicked(var.get())).pack()
# Radiobutton(root, text="Option 2", variable=var, value=2, command=lambda : clicked(var.get())).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

myLabel1 = Label(root, text=pizza.get())
myLabel1.pack()

if __name__ == "__main__":
    mainloop()

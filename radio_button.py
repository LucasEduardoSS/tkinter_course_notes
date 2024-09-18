from tkinter import *

# Root
root = Tk()
root.title('Creating Radio Buttons')
root.iconbitmap('images/draw_snake32.ico')


def clicked(value):
    myLabel1["text"] = value
    myLabel1.pack()


var = IntVar()

Radiobutton(root, text="Option 1", variable=var, value=1, command=lambda : clicked(var.get())).pack()
Radiobutton(root, text="Option 2", variable=var, value=2, command=lambda : clicked(var.get())).pack()

myLabel1 = Label(root, text=var.get())
myLabel1.pack()

if __name__ == "__main__":
    mainloop()

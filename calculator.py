# Build a simple calculator App

from tkinter import *

root = Tk()

terms = []
operators = []
results = []
cycle = 0
new_cycle = False


def button_click(number):
    global new_cycle
    if new_cycle:
        display.delete(0, END)
        new_cycle = False
    display.insert(END, number)


def button_clear():
    display.delete(0, END)


def button_operation(operation:str):
    if display.get() != '':
        terms.append(int(display.get()))

    match operation:
        case "add":
            op_symbol = "+"
        case "subtract":
            op_symbol = "-"
        case "multiply":
            op_symbol = "*"
        case "divide":
            op_symbol = "/"

    if len(operators) == len(terms) - 1:
        operators.append(op_symbol)
    display.delete(0, END)


def button_equal():
    terms.append(int(display.get()))
    display.delete(0, END)

    global cycle
    global results
    global new_cycle
    cycle_result = 0

    print('inicio', operators, terms, cycle)

    for i in range(0, len(operators)):
        if operators[i] == '+':
            cycle_result = terms[i] + terms[i + 1]
        elif operators[i] == '-':
            cycle_result = terms[i] - terms[i + 1]
        elif operators[i] == '*':
            cycle_result = terms[i] * terms[i + 1]
        elif operators[i] == '/':
            cycle_result = terms[i] / terms[i + 1]

        terms[i+1] = cycle_result

    results.append(int(cycle_result))
    display.insert(0, str(results[cycle]))
    cycle += 1
    terms.clear()
    operators.clear()
    new_cycle = True

    print('fim', operators, terms, cycle, results)


# Changes application name
root.title("Simple Calculator")

# Display
display = Entry(root, width=43, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
but_1 = Button(root, text="1", padx=30, pady=40, command=lambda: button_click(1))
but_2 = Button(root, text="2", padx=30, pady=40, command=lambda: button_click(2))
but_3 = Button(root, text="3", padx=30, pady=40, command=lambda: button_click(3))
but_4 = Button(root, text="4", padx=30, pady=40, command=lambda: button_click(4))
but_5 = Button(root, text="5", padx=30, pady=40, command=lambda: button_click(5))
but_6 = Button(root, text="6", padx=30, pady=40, command=lambda: button_click(6))
but_7 = Button(root, text="7", padx=30, pady=40, command=lambda: button_click(7))
but_8 = Button(root, text="8", padx=30, pady=40, command=lambda: button_click(8))
but_9 = Button(root, text="9", padx=30, pady=40, command=lambda: button_click(9))
but_0 = Button(root, text="0", padx=30, pady=40, command=lambda: button_click(0))

but_equal = Button(root, text="=", padx=29, pady=40, command=button_equal)
but_clear = Button(root, text="CL", padx=26, pady=40, command=button_clear)

but_add = Button(root, text="+ ", padx=27, pady=40, command=lambda: button_operation("add"))
but_sub = Button(root, text="-", padx=30, pady=40, command=lambda: button_operation("subtract"))
but_multiply = Button(root, text="*", padx=30, pady=40, command=lambda: button_operation("multiply"))
but_divide = Button(root, text="/", padx=30, pady=40, command=lambda: button_operation("divide"))

# Put the buttons on the screen
but_0.grid(row=4, column=0)
but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)
but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)
but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_clear.grid(row=4, column=1)
but_equal.grid(row=4, column=2)

but_add.grid(row=1, column=3)
but_sub.grid(row=2, column=3)
but_multiply.grid(row=3, column=3)
but_divide.grid(row=4, column=3)

root.mainloop()

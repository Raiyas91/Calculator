from _ast import Lambda
from tkinter import *
from tkinter import Button

root = Tk()
root.title("Simple Calculator")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=10, pady=10)

e = Entry(frame, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


button1 = Button(frame, text="1", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(1))
button2 = Button(frame, text="2", padx=43, pady=20, bg='LightSteelBlue3', command=lambda: button_click(2))
button3 = Button(frame, text="3", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(3))
button4 = Button(frame, text="4", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(4))
button5 = Button(frame, text="5", padx=43, pady=20, bg='LightSteelBlue3', command=lambda: button_click(5))
button6 = Button(frame, text="6", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(6))
button7 = Button(frame, text="7", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(7))
button8 = Button(frame, text="8", padx=43, pady=20, bg='LightSteelBlue3', command=lambda: button_click(8))
button9 = Button(frame, text="9", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(9))
button0 = Button(frame, text="0", padx=40, pady=20, bg='LightSteelBlue3', command=lambda: button_click(0))
button_add = Button(frame, text="+", padx=39, pady=20, bg='gray63', command=button_add)
button_equal = Button(frame, text="=", padx=91, pady=20, bg='thistle', command=button_equal)
button_clear = Button(frame, text="Clear", padx=81, pady=20, bg='thistle', command=button_clear)
button_sub = Button(frame, text="-", padx=41, pady=20, bg='gray63', command=button_sub)
button_mul = Button(frame, text="*", padx=42, pady=20, bg='gray63', command=button_mul)
button_div = Button(frame, text="/", padx=41, pady=20, bg='gray63', command=button_div)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()

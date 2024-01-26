from tkinter import *

r = Tk()
r.title("Calculator")
e = Entry(r, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

button1 = Button(r, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(r, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(r, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(r, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(r, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(r, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(r, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(r, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(r, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(r, text="0", padx=40, pady=20, command=lambda: button_click(0))
add = Button(r, text="+", padx=39, pady=20, command=button_add)
equals = Button(r, text="=", padx=93, pady=20, command=button_equal)
clear = Button(r, text="Clear", padx=90, pady=20, command=button_clear)

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
add.grid(row=5, column=0)
clear.grid(row=4, column=1, columnspan=2)
equals.grid(row=5, column=1, columnspan=2)

mainloop()
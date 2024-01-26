from tkinter import *
r = Tk()
r.geometry("1200x800")
r.title("Python 3 Quiz")
e = Entry(r, font="Aptos 20")
e.pack()

def myClick():
    myLabel = Label(r, text="Welcome, " + e.get() + " ! Get ready!")
    myLabel.pack()
myButton=Button(r, text="Confirm Name", fg="green", bg="red", state=ACTIVE, command=myClick)
myButton.pack()
mainloop()
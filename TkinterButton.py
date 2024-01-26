from tkinter import *
r = Tk()
def myClick():
    myLabel = Label(r, text="Fuck you")
    myLabel.pack()
myButton=Button(r, text="Click me", fg="green", bg="red", state=ACTIVE, command=myClick)
myButton.pack()
mainloop()
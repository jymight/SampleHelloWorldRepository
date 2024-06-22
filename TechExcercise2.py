
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Hello World Program")
window.geometry("800x600")

hello_message = tkinter.Message(window, text="Hello World!")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def show():
    color = clicked.get()
    window.config(bg=color)
    label.config(text=f"Background color changed to {color}")


options = [ 
    "Green", 
    "Blue", 
    "Red", 
    "Yellow", 
    "Purple", 
    "Pink", 
    "Orange"
] 


clicked = StringVar() 


clicked.set("Choose color") 


drop = OptionMenu(window, clicked, *options)
drop.pack()


button = Button(window, text="Modify Color", command=show).pack()


label = Label(window, text=" ")
label.pack()

window.mainloop()
import tkinter

window = tkinter.Tk()
window.title("Hello World Program")
window.geometry("1920x1080")

hello_message = tkinter.Message(window, text="Hello World!")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop()



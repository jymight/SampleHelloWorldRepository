import tkinter

window = tkinter.Tk()
window.title("Hello Chase's World")
window.geometry("1920x1080")

hello_message = tkinter.Message(window, text="Hello Chase's World!")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop()



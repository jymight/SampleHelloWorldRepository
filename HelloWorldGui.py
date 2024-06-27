import tkinter

window = tkinter.Tk()
window.title("Hello Jyair")
window.geometry("1280x720")

hello_message = tkinter.Message(window, text="Hello Jyair")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop()



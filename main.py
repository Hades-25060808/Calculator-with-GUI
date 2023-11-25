from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)

win.title("Calculator with GUI")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="grey",
                    highlightcolor="grey", highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=("arial", 18, "bold"), textvariable=input_text,
                    width=50, bg="#c7dcff", bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

button_fr = Frame(win, width=312, height=272.5, bg="grey")

button_fr.pack()

win.mainloop()

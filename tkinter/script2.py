from tkinter import *

window=Tk()

def kilogram_to_other():
    float_e1_value = float(e1_value.get())
    g = float_e1_value * 1000
    p = float_e1_value * 2.20462
    o = float_e1_value * 35.274
    t1.delete(1.0, END)
    t1.insert(END, g)
    t2.delete(1.0, END)
    t2.insert(END, p)
    t3.delete(1.0, END)
    t3.insert(END, o)

label=Label(window, text="Kg")
label.grid(row=0,column=0)

e1_value = StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1=Button(window, text="Convert", command=kilogram_to_other)
b1.grid(row=0,column=2)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
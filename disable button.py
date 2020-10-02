from tkinter import *
root = Tk()
var=stringvar()

def check():
    a=e1.Get()
    if(a)=="meena":
        b1.configure(state="active")
    else:
        print("no")
        b1.configure(state="disabled")
l1=Label(root,text="Enter name")
l1.pack()
e1=Entry(root,textvariable=var)
a=e1.get()
e1.pack()
b1=Button(root,text="submit",state="disabled")
b1.pack()
b2=Button(root,text="Validate Details!!",command=check)
b2.pack()

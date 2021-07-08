from tkinter import *
from tkinter import simpledialog as sd
import random
import string
from tkinter import ttk

def save():
    global dom
    dom = sd.askstring('Save','Name of the domain:')
    tree.insert("",END,text=dom,values=ent.get())
    ent.delete(0, END)


def gen():
    s1 = string.ascii_letters + string.punctuation+string.digits
    ent.delete(0,END)
    for i in range(10):
      ent.insert(0,random.choice(s1))


def log():
    frame2.tkraise()



w = Tk()
w.geometry('600x600')
frame2 = Frame(w)
frame2.grid(row=0,column=0,sticky=N+E+W+S)
frame1 = Frame(w)
frame1.grid(row=0,column=0,sticky=N+W+E+S)
lab = Label(frame1,text='Password:',font=('Helvetica',15))
lab.grid(row=1,column=0,padx=10,pady=50)
lab1 = Label(frame1,text='Check log for saved passwords',font=('Helvetica',10))
lab1.grid(row=3,column=0,padx=10,pady=30,columnspan=2)
ent = Entry(frame1,width=55,relief=GROOVE,bd=2)
ent.grid(row=1,column=1,columnspan=4)
but = Button(frame1,text='Save',relief=GROOVE,width=7,command=save)
but.grid(row=2,column=2)
but2 = Button(frame1,text='Generate',relief=GROOVE,width=7,command=gen)
but2.grid(row=2,column=3)
but3 = Button(frame1,text='Log',relief=GROOVE,width=7,command=log)
but3.grid(row=2,column=4)
tree = ttk.Treeview(frame2, column='1')
tree.heading('#0',text='Domain',anchor=W)
tree.heading('#1',text='Password',anchor=W)
tree.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
but4 = Button(frame2,text='Back',relief=GROOVE,width=7,command=frame1.tkraise)
but4.grid(row=2,column=2,sticky=E)
frame1.tkraise()
w.mainloop()
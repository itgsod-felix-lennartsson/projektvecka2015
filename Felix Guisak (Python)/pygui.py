from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()

def b1a():
   tkMessageBox.showinfo( None, "Ar du saker?")

def b2a():
   tkMessageBox.showinfo( None, "Va roligt! :)")

   
b1 = Tkinter.Button(top, text = "Tider", command = b1a, width = 20)
b2 = Tkinter.Button(top , text = "Test", command = b2a)

b1.pack()
b2.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Carl ar bast", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C2 = Checkbutton(top, text = "Felix ar bast", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C1.pack()
C2.pack()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

L1 = Label(top, text="User Name")
L1.pack()
E1 = Entry(top, bd = 2)

E1.pack()


C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

arc = C.create_oval(10, 50, 240, 210, fill="red")

C.pack()

top.mainloop()
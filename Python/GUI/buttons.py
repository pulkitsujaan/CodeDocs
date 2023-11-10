from tkinter import *
root=Tk()
root.geometry("400x500")

def printer():
    print("printed!!")
f1=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f1.pack()

b1=Button(f1,text="AYUSHI",command=printer)
b1.pack()

b2=Button(f1,text="GUNJAN",command=printer)
b2.pack()

b3=Button(f1,text="PULKIT",command=printer)
b3.pack()

b4=Button(f1,text="DADY",command=printer)
b4.pack()

b5=Button(f1,text="MUMMY",command=printer)
b5.pack()

root.mainloop()
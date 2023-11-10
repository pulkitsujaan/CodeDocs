from tkinter import *
root=Tk()
root.title("List Boxes")
root.geometry("455x233")
def add():
    global i
    lbx.insert(ACTIVE,i)
    i+=1
i=0
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First Item")
Button(root,text="Add Item",command=add).pack()
root.mainloop()
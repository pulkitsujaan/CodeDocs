from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
def order():
    tmsg.showinfo("Order recieved",f"Thanks for ordering....we have received your order for {var.get()}")
var = StringVar()
var.set("radio")
Label(root,text="What would you like to eat sir??",font="lucida 14 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Paneer",padx=14,variable=var,value="Paneer").pack(anchor="w")
radio=Radiobutton(root,text="bhindi",padx=14,variable=var,value="Bhindi").pack(anchor="w")
radio=Radiobutton(root,text="Chowmein",padx=14,variable=var,value="Chowmein").pack(anchor="w")

Button(text="Order Now!!",command=order,padx=3).pack()
root.mainloop()
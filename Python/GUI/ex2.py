from tkinter import *
root=Tk()
root.geometry("600x500")
def resize(event):
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")
# Label(text="Current size:600x500",font="timesnewroman 25 bold").grid(row=0,column=0)
heightvalue=StringVar()
widthvalue=StringVar()
Label(root,text="Height:").grid(row=1,column=0)
heightentry=Entry(root,textvariable=heightvalue)
heightentry.grid(row=1,column=1)

Label(root,text="Width:").grid(row=2,column=0)
heightentry=Entry(root,textvariable=widthvalue)
heightentry.grid(row=2,column=1)

apply=Button(root,text="Apply")
apply.grid()
apply.bind("<Button-1>",resize)
root.mainloop()
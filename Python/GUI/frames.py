from tkinter import *
root=Tk()
root.geometry("333x444")
frame1=Frame(root,bg="grey",borderwidth=7,relief=SUNKEN)
frame1.pack(side=LEFT,fill=Y)

frame2=Frame(root,bg="grey",borderwidth=7,relief=SUNKEN)
frame2.pack(side=TOP,fill=X)


l1=Label(frame1,text="Scrool",bg="grey")
l1.pack(side=LEFT)

l2=Label(frame2,text="Title Bar",bg="grey")
l2.pack(side=TOP)



root.mainloop()
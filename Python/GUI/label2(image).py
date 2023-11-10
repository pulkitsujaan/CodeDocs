from tkinter import *
root=Tk()
root.geometry("800x900")
photo=PhotoImage(file="Marvel.png")
label=Label(text="Hello World",image=photo)
label.pack()

root.minsize(100,100)
root.mainloop()
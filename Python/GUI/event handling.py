from tkinter import *
root=Tk()
root.title("Event handling")
root.geometry("644x344")
def clickable(event):
    print(f"Button clicked at {event.x},{event.y}")
widget=Button(root,text="Click me!!")
uservalue=StringVar()
entry=Entry(root,textvariable=uservalue)
entry.pack()
widget.pack()
widget.bind("<Button-1>",clickable)
entry.bind("q",quit)
root.mainloop()
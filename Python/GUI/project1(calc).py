from tkinter import *
root=Tk()
root.geometry("300x350")
root.title("Calculator")

def click(event):
    global calculation_value
    text=event.widget.cget("text")
    # print(text)
    if text=="=":
        if calculation_value.get().isdigit():
            value=int(calculation_value.get())
        else:
            value=eval(entry.get())
        calculation_value.set(value)
        entry.update()
    elif text=="C":
        calculation_value.set("")
        entry.update()
    else:
        calculation_value.set(calculation_value.get()+ text)
        entry.update()

calculation_value=StringVar()
calculation_value.set("")

entry=Entry(root,textvariable=calculation_value,font="lucida 40 bold")
entry.pack()

# 7 8 9
f=Frame(root,bg="grey")

b=Button(f,text="7",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="9",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

# 4 5 6
f=Frame(root,bg="grey")

b=Button(f,text="4",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="6",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

# 1 2 3
f=Frame(root,bg="grey")

b=Button(f,text="1",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="3",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

# . 0 =
f=Frame(root,bg="grey")

b=Button(f,text=".",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="0",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

#C 00 =
f=Frame(root,bg="grey")

b=Button(f,text="C",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="00",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="(",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text=")",padx=12,pady=9, font="lucida 15 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
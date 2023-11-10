from tkinter import *
class Calculator(Tk):
    def __init__(self,string):
        self.calculation_value=StringVar()
        self.calculation_value.set("")

        entry=Entry(self,textvariable=self.calculation_value,font="lucida 40 bold")
        entry.pack()
        self.contentlist=string.split(" ")

        self.f=Frame(self,bg="grey")

        self.b=Button(self.f,text=self.contentlist[0],padx=12,pady=9, font="lucida 15 bold")
        self.b.pack(side=LEFT)
        self.b.bind("<Button-1>",self.click)

        self.b=Button(self.f,text=self.contentlist[1],padx=12,pady=9, font="lucida 15 bold")
        self.b.pack(side=LEFT)
        self.b.bind("<Button-1>",self.click)

        self.b=Button(self.f,text=self.contentlist[2],padx=12,pady=9, font="lucida 15 bold")
        self.b.pack(side=LEFT)
        self.b.bind("<Button-1>",self.click)

        self.b=Button(self.f,text=self.contentlist[3],padx=12,pady=9, font="lucida 15 bold")
        self.b.pack(side=LEFT)
        self.b.bind("<Button-1>",self.click)

        self.f.pack()
    
    def click(self,event):
        # global self.calculation_value
        self.text=event.widget.cget("text")
        # print(text)
        if self.text=="=":
            if self.calculation_value.get().isdigit():
                value=int(self.calculation_value.get())
            else:
                value=eval(self.entry.get())
            self.calculation_value.set(value)
            self.entry.update()
        elif self.text=="C":
            self.calculation_value.set("")
            self.entry.update()
        else:
            self.calculation_value.set(self.calculation_value.get()+ self.text)
            self.entry.update()
first_row=Calculator("7 8 9")
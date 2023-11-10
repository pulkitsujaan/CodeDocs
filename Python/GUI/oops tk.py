'''
mauj krdi, ae bete
OOPs ke through to mauj krdi bete
'''

from tkinter import *
class GUI(Tk):
    # 'root' is 'self' here
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvariable=self.var,relief=SUNKEN,anchor=W)
        self.statusbar.pack(fill=X,side=BOTTOM)
    def entry(self):
        self.entryvar=StringVar()
        self.entrywidget=Entry(self,textvariable=self.entryvar)
        self.entrywidget.pack(pady=25)
    def printed(self):
        print(self.entryvar.get())
        pass
    def createbutton(self,inputtext):
        Button(text=inputtext,command=self.printed).pack(pady=25)
if __name__=='__main__':
    # root is window object here
    window=GUI()
    window.status()
    window.entry()
    window.createbutton("Print Here")
    window.mainloop()
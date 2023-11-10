from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("500x400")
root.title("File Menu")

def printer():
    print("Hell Function")
def helpfunc():
    tmsg.showinfo("Help","This is a GUI help....")

def rateus():
    exp=tmsg.askquestion("Rate Us","Was your experience good?")
    if exp=="yes":
        msg="Thank You...Please rate us on App Store also..."
    else:
        msg="Please tell us what went wrong...we will contact you soon..."
    tmsg.showinfo("Experience",msg)
def fail():
    ans=tmsg.askretrycancel("Not able....","Not able to convince teacher, tum fail ho")
    if ans:
        tmsg.showinfo("Nikal","retry krke koi fayeda nhi h bhai...tu fail h to fail hi rahega")
    else:
        tmsg.showinfo("Nikal","Good!! Ab kro dobara poori class...")
def tatti():
    ans=tmsg.askquestion("Btao Bay","Tune Tatti khaani chhod di kya??")
    if ans=='yes':
        tmsg.showinfo("Kya??","Pehle khata tha kya?? XD")
    else:
        tmsg.showinfo("Wht??","Ab bhi khata h??  XD")
#use these to create a non drop-down menu
# menu=Menu(root)
# menu.add_command(label="File",command=printer)
# menu.add_command(label="Quit",command=quit)
# root.config(menu=menu)

mainmenu=Menu(root)

menufile=Menu(mainmenu,tearoff=0)
menufile.add_command(label="Open",command=printer)
newopt=Menu(menufile,tearoff=0)
newopt.add_command(label="Python File",command=printer)
newopt.add_command(label="Java File",command=printer)
menufile.add_cascade(label="New",menu=newopt)

menufile.add_separator()
menufile.add_command(label="Save",command=printer)
menufile.add_command(label="Save As",command=printer)
menufile.add_command(label="Print",command=printer)
mainmenu.add_cascade(label="File",menu=menufile)



menuedit=Menu(mainmenu,tearoff=0)
menuedit.add_command(label="Copy",command=printer)
menuedit.add_command(label="Font",command=printer)
menuedit.add_separator()
menuedit.add_command(label="Find and Replace",command=printer)
menuedit.add_command(label="Toggle Word Wrap",command=printer)
mainmenu.add_cascade(label="Edit",menu=menuedit)

menuhelp=Menu(mainmenu,tearoff=0)
menuhelp.add_command(label="help",command=helpfunc)
menuhelp.add_command(label="Rate Us",command=rateus)
menuhelp.add_command(label="Exam ki Sifarish",command=fail)
menuhelp.add_command(label="Tatti",command=tatti)
mainmenu.add_cascade(label="Help",menu=menuhelp)

root.config(menu=mainmenu)
root.mainloop()
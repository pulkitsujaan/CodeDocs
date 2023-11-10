from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("File Menu")

def printer():
    print("Hell Function")

#use these to create a non drop-down menu
# menu=Menu(root)
# menu.add_command(label="File",command=printer)
# menu.add_command(label="Quit",command=quit)
# root.config(menu=menu)

menu2=Menu(root)

menusub1=Menu(menu2,tearoff=0)
menusub1.add_command(label="Open",command=printer)
# menusub1.add_command(label="New",command=printer)
sub1ka1=Menu(menusub1,tearoff=0)
sub1ka1.add_command(label="Python File",command=printer)
sub1ka1.add_command(label="Java File",command=printer)
menusub1.add_cascade(label="New",menu=sub1ka1)

menusub1.add_separator()
menusub1.add_command(label="Save",command=printer)
menusub1.add_command(label="Save As",command=printer)
menusub1.add_command(label="Print",command=printer)
menu2.add_cascade(label="File",menu=menusub1)



menusub2=Menu(menu2,tearoff=0)
menusub2.add_command(label="Copy",command=printer)
menusub2.add_command(label="Font",command=printer)
menusub2.add_separator()
menusub2.add_command(label="Find and Replace",command=printer)
menusub2.add_command(label="Toggle Word Wrap",command=printer)
menu2.add_cascade(label="Edit",menu=menusub2)
root.config(menu=menu2)
root.mainloop()
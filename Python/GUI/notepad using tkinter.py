from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo
import os
if __name__=='__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    # file menu options
    def newFile():
        global CurrentFile
        root.title("Untitled - Notepad")
        CurrentFile=None
        TextArea.delete(1.0, END)
        root.mainloop()
    def openFile():
        global CurrentFile
        CurrentFile=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text document","*.txt")])
        if CurrentFile == "":
            CurrentFile=None
        else:
            root.title(os.path.basename(CurrentFile)+" - Notepad")
            TextArea.delete(1.0,END)
            f=open(CurrentFile,'r')
            TextArea.insert(1.0,f.read())
            f.close
    def saveFile():
        global CurrentFile
        if CurrentFile ==None:
            CurrentFile=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text document","*.txt")])
            if CurrentFile=="":
                CurrentFile=None
            else:
                # Save as a new file
                f=open(CurrentFile,'w')
                f.write(TextArea.get(1.0,END))
                f.close()
                root.title(os.path.basename(CurrentFile)+" - Notepad")
        else:
            f=open(CurrentFile,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
    def exitNotepad():
        root.destroy()
    
    # edit menu options
    def Cut():
        TextArea.event_generate(("<<Cut>>"))
    def Copy():
        TextArea.event_generate(("<<Copy>>"))
    def Paste():
        TextArea.event_generate(("<<Paste>>"))

    # help menu Options
    def Help():
        showinfo("Notepad","Kya help chahiye bay?? notepad bhi ni chalana aata...")
    def About():
        showinfo("Notepad","hai nee badhiya notepad...")

    # add a scroll bar to the notepad
    ScrollBar=Scrollbar(root)
    ScrollBar.pack(fill=Y,side=RIGHT)

    #add text area
    TextArea=Text(root,font="lucida 13",yscrollcommand=ScrollBar.set)
    TextArea.pack(fill="both",expand=True)
    
    #this is the file in which we are working
    CurrentFile=None


    # configure the scroll bar
    ScrollBar.config(command=TextArea.yview)


    #menubar
    MenuBar=Menu(root)
    
    # file menu
    FileMenu=Menu(MenuBar,tearoff=0)
    #new file option in file menu
    FileMenu.add_command(label="New",command=newFile)
    #Open file option in file menu
    FileMenu.add_command(label="Open",command=openFile)
    #Save file option in file menu
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=exitNotepad)
    MenuBar.add_cascade(label="File",menu=FileMenu)

    # edit menu
    EditMenu=Menu(MenuBar,tearoff=0)
    #new file option in file menu
    EditMenu.add_command(label="Cut...  Ctrl+X",command=Cut)
    EditMenu.add_command(label="Copy... Ctrl+C",command=Copy)
    EditMenu.add_command(label="Paste...    Ctrl+V",command=Paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    
    # help menu
    HelpMenu=Menu(MenuBar,tearoff=0)
    #new file option in file menu
    HelpMenu.add_command(label="Help",command=Help)
    HelpMenu.add_command(label="About Us",command=About)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)

    # configure menubar
    root.config(menu=MenuBar)

    root.mainloop()
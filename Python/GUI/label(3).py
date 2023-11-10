from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry("500x400")
root.maxsize(500,400)
root.title("Pulkit Basic GUI")

# Some important label Attributes
    # text--adds text
    # bg--background
    # fg--foreground
    # font--sets the font
        # 1.font=("fontname", fontsize, blod/italic)
        # 2.font="fontname fontsize bold/italic"
    # padx--padding x
    # pady--padding Y
    # relief--border styling --SUNKEN, RAISED, GROOVE, RIDGE

label=Label(text="Ready",bg="dark green",fg="white",pady=1,font="algerian 12 bold italic")


# Some important pack attributes
    # anchor--direction--nw,ne,sw,se
    # side--if you want your label in bottem or other side--TOP,BOTTOM,RIGHT,LEFT
    # fill--fill=X,fill=Y
    # padx,pady--padding x,padding y
label.pack(side=BOTTOM, fill=X,pady=2,padx=2)



root.mainloop()
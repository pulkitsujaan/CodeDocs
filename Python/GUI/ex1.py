'''Newspaper'''
from tkinter import *
from PIL import Image
root=Tk()
root.title("Newspaper")
root.geometry("1000x800")
news=[]
images=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        news.append(text)
    # TODO:Resize the images
    image=Image.open(f"{i+1}.png")
    newimage=image.resize((225, 225),Image.ANTIALIAS)
    images.append(PhotoImage(newimage))
f0=Frame(root,width=800,height=70)
Label(root,text="Dainik Jagran English",font="algerian 33 bold").pack()
Label(root,text="March 10, 2021",font="algerian 13 bold").pack()
f0.pack()


f1=Frame(root,width=900,height=200)
Label(root,text=news[0]).pack(side=LEFT)
Label(root,image=images[0]).pack(anchor="e")
# f2=Frame(root,width=900,height=200)
# f3=Frame(root,width=900,height=200)
f1.pack()
root.mainloop()
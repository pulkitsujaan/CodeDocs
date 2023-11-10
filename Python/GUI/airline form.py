from tkinter import *
root=Tk()
root.geometry("644x344")
import time
def getval():
    print("Registering")
    with open("records(airline).txt",'a') as f:
        f.write(f"[{namevalue.get()},{phonevalue.get()},{Sexvalue.get()},{Emergencyvalue.get()},{Ticketvalue.get()}]\n")
    time.sleep(2)
    print("Done Registering your ticket...we will contact you soon!!")
Label(text="Welcome to Sujaan Airlines",font="algerian 20 bold",pady=15).grid(row=0,column=3)

name=Label(root, text="Name")
phone=Label(root, text="Phone No.")
Sex=Label(root, text="Sex")
Emergency=Label(root, text="Emergency Contact")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
Sex.grid(row=3,column=2)
Emergency.grid(row=4,column=2)


namevalue=StringVar()
phonevalue=StringVar()
Sexvalue=StringVar()
Emergencyvalue=StringVar()
Ticketvalue=IntVar()


nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
Sexentry=Entry(root,textvariable=Sexvalue)
Emergencyentry=Entry(root,textvariable=Emergencyvalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
Sexentry.grid(row=3,column=3)
Emergencyentry.grid(row=4,column=3)



Ticketentry=Checkbutton(text="Are you going as a business class?", variable=Ticketvalue)
Ticketentry.grid(row=5,column=3)

Button(text="Register",command=getval).grid(row=6,column=3)
root.mainloop()
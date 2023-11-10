import datetime

def pulkit():   
    enter_show=input("What do you want to do?\n\n 1. for enter data\n2. for retrieve data\n")
        
    #for enter data
    if(enter_show=='1'):
        exer_diet=input("\n1.For Exercise\n2.for Diet\n\n\n")

    # for diet enter
    if(exer_diet=='2'):
        f=open("pulkit_diet.txt","w")
        f.write(input("Enter data\n"))
        print("Write succesfull.")
                

    # for exercise enter
    elif(exer_diet=='1'):
        f=open("pulkit_exer.txt","a")
        a=input("enter data")
        f.write(f"[{getdate()}]{a}")
        print("Write succesfull")
                      



    # for retrieve data 
    elif(enter_show=='2'):
        exer_diet=input("\n1.For Exercise\n2.for Diet\n\n\n")
            
    # for diet retrieve
    if(exer_diet=='2'):
        print(open("pulkit_diet.txt","r").read())
                

    # for exercise retrieve
    elif(exer_diet=='1'):
        print(open("pulkit_exer.txt","r").read())
def client_name():
    name=input("What is your name?\n\n1. for Pulkit\n2. for Gunjan\n3. for Ayushi\n")
    return name
def getdate():
    return datetime.datetime.now()
name=client_name()

if(name=='1'):
    pulkit()
elif(name=='2'):
    gunjan()
elif(name=='3'):
    ayushi()
else:
    print("You have not entered a valid data")


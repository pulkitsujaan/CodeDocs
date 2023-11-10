print("---All marks out of 100---")
phy=int(input("Enter marks in physics: "))
chem=int(input("Enter marks in chemistry: "))
maths=int(input("Enter marks in maths:"))

percent=(phy+chem+maths)/3
if percent<40:
    print("Sorry! You are fail!")
elif percent>=40 and phy>=33 and maths>=33 and chem>=33:
    print("Congrats! You are Pass!")
else:
    print("Sorry! You are fail!")
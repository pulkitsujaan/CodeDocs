name=input("What is your name?\n")
if name.isnumeric():
    raise TypeError("Numbers are not allowed...")
print(f"\nHello {name}\n")
Class=input("In which class you're?\n")
if int(Class)==0:
    raise ZeroDivisionError("\nSahi se likh le class ka naam...")
print(f"\nAll the best! for your exams...")
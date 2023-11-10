currentage=int(input("Enter your age or year of birth....\n"))
if currentage>=1000 and currentage<2021:
    currentage=2021-currentage
elif currentage>2021 or currentage==0:
    print("Abbe paida to ho ja pehle")
    exit()
print(f"You will be 100 years old in the year {currentage+2021+100}")
opt=input("Do you want to check what will be your age in a particular year?(y/n)")
if opt=='y':
    year=int(input("Enter the year you want ot check your age...."))
    print(f"Your age in the year {year} will be {(year-2021)+currentage}")
else:
    print("Thanks for using this program...")
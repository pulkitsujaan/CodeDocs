grades=int(input("Enter your grades: "))
if grades>=90 and grades<=100:
    print("Grade: Ex")
elif grades>=80:
    print("Grade: A")
elif grades>=70:
    print("Grade: B")
elif grades>=60:
    print("Grade: C")
elif grades>=50:
    print("Grade: D")
elif grades<50 and grades>=0:
    print("Grade: F")
else:
    print("Sahi grades daal bsdk!")
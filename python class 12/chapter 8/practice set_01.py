def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return print(f"Greatest: {n1}")
    if n2>n1 and n2>n3:
        return print(f"Greatest: {n2}")
    if n3>n2 and n3>n1:
        return print(f"Greatest: {n3}")

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

greatest(num1,num2,num3)
'''factorial'''
num=int(input("Enter a number: "))
i=num
fact=1
while i>=1:
    fact*=i
    i-=1
print(f'Factorial: {fact}')
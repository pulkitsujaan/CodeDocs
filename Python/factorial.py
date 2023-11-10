"""This is a program to check factorial of numbers upto 999"""
#remove the hash tag from the next line to make the code run endlessly
# while(True):
    
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number to check its factorial\n"))
fact=factorial(num)
print(f"Factoriaal of {num} is {fact}")

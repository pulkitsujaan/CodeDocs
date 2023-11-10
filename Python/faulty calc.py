print("Hello, this is your own calculator\n\n'/' for divide\n'*' for multiply\n'-' for subtraction\n'+' for addition")
sign=input("\n\nEnter the operator you want to use\n")
num1=input("Enter first number\n")
num2=input("Enter second number\n")
if(sign=='+' and (num1=='56' and num2=='9') or (num2=='56' and num1=='9') ):
    print("LOL")
    
elif(sign=='*' and (num1=='45' and num2=='3') or (num2=='45' and num1=='3') ):
    print("LOL")
    
elif(sign=='/' and (num1=='56' and num2=='6') or (num2=='56' and num1=='6') ):
    print("LOL")
    
else:
    num1_real=int(num1)
    num2_real=int(num2)
    if(sign=='+'):
        print(num1_real + num2_real)
    elif(sign=='-'):
        print(num1_real - num2_real)
    elif(sign=='*'):
        print(num1_real * num2_real)
    elif(sign=='/'):
        print(num1_real / num2_real)

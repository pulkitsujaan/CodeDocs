# methods with double underscore are called dunder methods
class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,number):
        print("Addition")
        return self.num + number.num
    
    def __mul__(self,number):
        return self.num * number.num

num1=Number(10)
num2=Number(20)
print(num1+num2)
mul=num1*num2
print(mul)

''''
https://docs.python.org/3/reference/datamodel.html#:~:text=3.3.8.-,Emulating,-numeric%20types%C2%B6

https://www.geeksforgeeks.org/operator-overloading-in-python/

'''
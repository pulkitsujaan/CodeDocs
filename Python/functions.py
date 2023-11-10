"""
2 types of function:
1.built in function----jo pehle se aate h
2.user defined function---jo hum khud banate h

"""

"""
#example of builtin function
a=5
b=23
c=sum((a,b))
#print(c)
"""


"""
#user defined function syntax
def function1():
    print("Hello, this is a user defined function")
print(function1())  #none print hoga, as a return value
"""


"""
#function that take value
def function2(x, y):
    print("sum of", x,"and", y, "is", x+y)
function2(12, 667)
"""


"""
#function that return value

def function3(a, b):
   """ """this is a function to calculate the average of 2 numbers""" """
   #this is a docstring i.e. a description of a function
    aver_fake=(a+b)/2
    return aver_fake
aver_real=function3(5, 8)
#print(aver)
print(function3.__doc__)
"""
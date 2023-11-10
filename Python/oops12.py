class A:
    classvar1="This is a class variable"
    def __init__(self):
        self.instancevar44="This is a instance variable of class A"
        self.instancecar2="This is an instance variable 2 of class A"
class B(A):
    classvar1="This is a class variable"
    def __init__(self):
        super().__init__()#important
        self.instancevar="This is a instance variable of class B"
        self.instancevar2="This is an instance variable 2 of class B"
a=A()
b=B()
print(b.instancevar44)#to access the variable of class A, you have to use the method super
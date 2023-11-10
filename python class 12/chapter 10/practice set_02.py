class calculator():
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def sqRoot(self):
        print(f"Square Root of {self.num} is {self.num**0.5}")


num1=calculator(9)
num1.square()
num1.cube()
num1.sqRoot()

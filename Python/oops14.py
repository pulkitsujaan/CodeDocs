"""Public, protected, private access specifiers"""
class elec_device:
    power="Electricity"
    def __init__(self, name, cost, size):#init is a dunder method
        self.name=name
        self.cost=cost
        self.size=size
    def info(self):
        return f"My name is {self.name}, My cost is Rs.{self.cost} and I am a {self.size} size device"
    def __add__(self, other):
        return self.cost + other.cost
    def __sub__(self, other):
        return self.cost - other.cost
    def __eq__(self, other):
        return self.cost == other.cost
    def __ge__(self, other):
        return self.cost >= other.cost
dev1=elec_device("Fridge",20000,"Large")
dev2=elec_device("printer",10000,"medium")
print(dev1 + dev2)
print(dev1 - dev2)
print(dev1 == dev2)
print(dev1 >= dev2)
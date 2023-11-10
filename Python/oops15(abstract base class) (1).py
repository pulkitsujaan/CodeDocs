from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def peri(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def peri(self):
        return f"Perimeter of this rectangle is {2*(self.length+self.breadth)}"
class triangle(Shape):
    type = "Triangle"
    sides = 3
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def peri(self):
        return f"Perimeter of this triangle is {self.side1+self.side2+self.side3}"
shp1=Rectangle(5,4)
shp2=triangle(5,3,7)
print(shp2.peri())
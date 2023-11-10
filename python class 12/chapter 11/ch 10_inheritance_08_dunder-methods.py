class Number:
    def __init__(self,num):
        self.num=num
    # def __add__(self,number):
    #     print("Addition")
    #     return self.num + number.num
    
    # def __mul__(self,number):
    #     return self.num * number.num
    
    def __str__(self):#print something meaningful instead of object definition
        return f"Object: {self.num}"
    def __len__(self):#define length of object
        return 1

nam=Number(10)
print(nam)
print(len(nam))
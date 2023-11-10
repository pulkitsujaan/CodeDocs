#setter aur deleter abstract base class(ABC) ke naam se hi banana h
#setter aur deleter hum tab use krte hain jab hume vo instance delete krna ko jo humne manually nhi banaya
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property
    def details(self):
        return f"Employee Name is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "E-mail is not set yet"
        else:
            return f"{self.lname}.{self.fname}@pulkitkicompany.com"
    @email.setter
    def email(self, string):
        print("Setting Now....")
        names= string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


emp1=employee("Pulkit","Sujaan")
emp2=employee("ayushi","sujaan")
#object introspection
import inspect
# print(dir(emp2))
# print(id(emp2))
# print(type(emp2))
print(inspect.isabstract(emp2))
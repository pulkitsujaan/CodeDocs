'''OOPS'''
class Employee:
    company='google'#class attribute
    salary=1_00_000
    def GetSalary(self):
        print(f'{self.name} working in {self.company} has a salary {self.salary}rs')

    # Static methods are used when we don't want to use self parameter in the method
    @staticmethod
    def MorningWish():
        print("Good Morning!!")
    

pulkit=Employee()#instance of class Employee

#instance attribute
pulkit.name="Pulkit"
pulkit.salary=100


# we can also change the class attributes during the code
Employee.company="Meta"

pulkit.GetSalary()#equivalent to Employee.GetSalary(pulkit)
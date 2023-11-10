# init method------constructor method
class Employee:
    def __init__(self,name,salary,subCompany):
        print("Employee Created!")
        self.name=name
        self.salary=salary
        self.subCompany=subCompany
    
    company='google'
    salary=1_00_000
    
    def GetSalary(self):
        print(f'{self.name} working in {self.company} has a salary {self.salary}rs')
    @staticmethod
    def MorningWish():
        print("Good Morning!!")

    def GetDetails(self):
        print(f'Name:{self.name}\nSalary:{self.salary}\nSubBranch:{self.subCompany}')

pulkit=Employee("Pulkit",1_00_000,'BardAI')
pulkit.GetDetails()
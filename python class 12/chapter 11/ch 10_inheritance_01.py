class Employee:
    company='google'
    def showDetails(self):
        print('This is an Employee')

class Programmer(Employee):
    language='Python'
    company='Youtube'
    def name(self):
        print("This is a programmer")
    
a=Employee()
a.showDetails()
p=Programmer()
p.name()
print(a.company)
print(p.company)
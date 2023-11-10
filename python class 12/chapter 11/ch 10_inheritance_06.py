# it makes the function to be usable as a property 
class Employee:
    company="Baghban"
    salary=900
    bonus=100

    @property
    def total_salary(self):
        return self.salary+self.bonus
    
    @total_salary.setter
    def total_salary(self,val):
        self.bonus=val-self.salary

mai=Employee()
print(mai.total_salary)
mai.total_salary=1500
print(mai.bonus)
print(mai.total_salary)
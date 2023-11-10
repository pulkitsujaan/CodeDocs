class Employee():
    salary=1000
    increment=2
    
    @property
    def incr_salary(self):
        return self.salary*self.increment
    
    @incr_salary.setter
    def incr_salary(self,sai):
        self.increment=sai/self.salary

e=Employee()
print(e.salary)
print(e.increment)

e.incr_salary=10000
print(e.incr_salary)
print(e.increment)

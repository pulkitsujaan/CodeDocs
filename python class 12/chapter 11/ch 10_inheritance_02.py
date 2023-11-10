'''Multiple Inheritance---Inheriting from more than one class'''


class father:
    gender='male'
    country='India'
class mother:
    gender='female'
    country='Pakistan'
class son(father, mother):
    country='USA'
    def breath(self):
        print("Breathing...")
class daughter(mother,father):
    country='USA'
    def breath(self):
        print("Breathing...")

vijay=father()
suman=mother()
pulkit=son()
gunjan=daughter()


#preference given to that class which is written first during definition
print(pulkit.gender)
print(gunjan.gender)
pulkit.breath()
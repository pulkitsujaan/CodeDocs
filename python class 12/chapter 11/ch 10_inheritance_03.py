'''Multi-level Inheritance'''

class grandfather():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    gender='male'
    def breath(self):
        print("Breathing")

class father(grandfather):
    gender='F-male'
    def walk(self):
        print('Walking')
class you(father):
    def talk(self):
        print("talking")

hariram=grandfather("hari",90)
pulkit=you("Pulkit",17)
pulkit.breath()
pulkit.walk()
pulkit.talk()
print(pulkit.gender)
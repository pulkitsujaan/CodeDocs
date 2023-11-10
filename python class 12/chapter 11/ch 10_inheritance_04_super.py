class grandfather():
    gender='male'
    
    def __init__(self):
        print("Creating Grandfather...")
    
    def breath(self):
        print("Breathing")

class father(grandfather):
    gender='F-male'
    
    def __init__(self):
        super().__init__()#calls the constructor of it's super class
        print("Creating Father...")
    
    def walk(self):
        print('Walking')

class you(father):
    def __init__(self):
        super().__init__()
        print("Creating your character!")
    
    def talk(self):
        super().walk()#calls the walk method from its super class
        print("talking")

pulkit=you()
# pulkit.talk()
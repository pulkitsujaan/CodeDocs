class Programmer():
    company='Microsoft'
    def __init__(self,name,age,SubBranch):
        self.name=name
        self.age=age
        self.Branch=SubBranch
    def getDetails(self):
        print(f'Company----{self.company}\nName:{self.name}\nAge:{self.age}\nBranch:{self.Branch}')

pulkit=Programmer('Pulkit',16,'Marketing')
shobhit=Programmer('Shobhit',11,'Front-End Development')    
gunjan=Programmer('Gunjan',19,'Back-End Development')

shobhit.getDetails()
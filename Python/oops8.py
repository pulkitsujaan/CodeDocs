"""Multi Inheritance"""
class Taps:
    import random
    time="7 to 12:30"
    def __init__(self,name,Class,section):#constructor
        self.name=name
        self.Class=Class
        self.section=section
    def info(self):
        return f"Name:{self.name}\nClass:{self.Class}\nSection:{self.section}"

    @classmethod
    def changeTime(cls, newTime):
        cls.time=newTime
    @classmethod
    def from_dash(cls, string):
        # parameters=string.split("-")
        # return cls(parameters[0],parameters[1],parameters[2])
        return cls(*string.split("-"))
    @staticmethod
    def printrandom(string):
        print("You said "+string)
pulkit=Taps#("Pulkit","9th","akash")
gunjan=Taps#("Gunjan","11th", "PCM")
ayushi=Taps.from_dash("ayushi-passout-passout")
class player:
    no_of_game=4
    def __init__(self, name, game):
        self.game=game
        self.name=name
    def printdetails(self):
        return f"Name:{self.name}\nGame:{self.game}"

class coolguy(Taps, player):
    pass
dhruv=player("dhruv","football")

jeetu=coolguy("Jeetu","Pass out","cool")
print(jeetu.info())
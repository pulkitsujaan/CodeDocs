#static method use
#static method hote hain jab hume na to class use krni ho na instance variables
class Taps:
    import random
    time="7 to 12:30"
    def __init__(self,name,Class,section):
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
print(ayushi.name)
Taps.printrandom("Pulkit")
# pulkit.name="Pulkit"
# pulkit.Class="9th"
# pulkit.section="akash"

# gunjan.name="gunjan"
# gunjan.Class="11th"
# gunjan.section="PCM"

# print(pulkit.time)
# pulkit.changeTime("9 to 6")
# print(pulkit.time)
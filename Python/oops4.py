class Taps:
    time="7 to 12:30"
    # def __init__(self,name,Class,section):
    #     self.name=name
    #     self.Class=Class
    #     self.section=section
    def info(self):
        return f"Name:{self.name}\nClass:{self.Class}\nSection:{self.section}"

    @classmethod
    def changeTime(cls, newTime):
        cls.time=newTime
pulkit=Taps#("Pulkit","9th","akash")
gunjan=Taps#("Gunjan","11th", "PCM")
# print(pulkit.section)

pulkit.name="Pulkit"
pulkit.Class="9th"
pulkit.section="akash"

gunjan.name="gunjan"
gunjan.Class="11th"
gunjan.section="PCM"

print(pulkit.time)
pulkit.changeTime("9 to 6")
print(pulkit.time)
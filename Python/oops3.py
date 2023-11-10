class Taps:
    def __init__(self,name,Class,section):
        self.name=name
        self.Class=Class
        self.section=section
    def info(self):
        return f"Name:{self.name}\nClass:{self.Class}\nSection:{self.section}"
pulkit=Taps("Pulkit","9th","akash")
gunjan=Taps("Gunjan","11th", "PCM")
print(pulkit.section)

# pulkit.name="Pulkit"
# pulkit.Class="9th"
# pulkit.section="akash"

# gunjan.name="gunjan"
# gunjan.Class="11th"
# gunjan.section="PCM"

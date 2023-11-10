"""Public, protected, private access specifiers"""
class elec_device:
    runtime="Voltage"
    runtime2="Battery"
    _protect="Protected variable"#use single _ to make a var private
    __private="Private Variable"#use double _ to make a var private
    def howtoRun(self):
        return f"I run either on {self.runtime} or {self.runtime2}"
class pocket_gadgets(elec_device):
    runtime="Battery"
    runtime2="Charger"
    def howtoRun(self):
        return f"I can run either on {self.runtime} or {self.runtime2}"
class phone(pocket_gadgets):
    runtime="Battery"
    def howtoRun(self):
        return f"I can run on {self.runtime}"
fridge=elec_device()
print(fridge._elec_device__private)
#to acccess a private variable use this-----object._CLASS NAMEvariablename
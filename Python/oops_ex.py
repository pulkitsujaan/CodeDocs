class elec_device:
    runtime="Voltage"
    runtime2="Battery"
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
ipod=pocket_gadgets()
oppo=phone()
print(oppo.howtoRun())
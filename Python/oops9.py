class Grandfather:
    basketball="level 10"
class Father(Grandfather):
    dance=2
    basketball="Level 5"
    def isdance(self):
        return f"I can dance in {self.dance} different forms"
class Me(Father):
    dncforms=6
    def isdance(self):
        return f"I can dance in {self.dncforms} differnet forms"
hari=Grandfather()
Vijay=Father()
Pulkit=Me()
print(Pulkit.isdance())
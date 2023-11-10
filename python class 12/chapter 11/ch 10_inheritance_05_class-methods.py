# class methods change the atrributes of class
class human:
    name='Homosapian'
    age=69

    @classmethod
    def change_age(cls,Age):
        cls.age=Age

pulkit=human()
print(human.age)
print(f'{pulkit.age}\n')
pulkit.change_age(100)
print(human.age)
print(pulkit.age)
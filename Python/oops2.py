class Taps:
    """This is the docstring"""
    time="7:00~12:30"
    pass
pulkit=Taps()
gunjan=Taps()

pulkit.name="Pulkit"
pulkit.Class=9
pulkit.section="akash"

gunjan.name="gunjan"
gunjan.Class=11
gunjan.section="PCM"
print(Taps.time)
Taps.time="10:00~3:00"
print(Taps.time)
gunjan.time="7:30~1:30"
print(Taps.__dict__)
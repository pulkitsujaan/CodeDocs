def cels_to_far(temp):
    temp=(temp*1.8) + 32
    return temp
cels=int(input("Enter temperature in Celsius: "))
farhen=cels_to_far(cels)
print(farhen)
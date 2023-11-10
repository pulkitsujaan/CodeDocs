"""
to ask to enter a number
if number bigger than 100 then congratulate
if smallar than 100 then try again
"""
print("Enter a number")
while(True):
    a=int(input())
    if(a<100):
        print("try again")
        continue
    else:
        print("Congratulations, you've entered a no. bigger than 100")
        break
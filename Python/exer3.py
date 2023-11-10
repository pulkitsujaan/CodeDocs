"""
----GAME----
declare a number
ask user to guess the no. and give him a range
user should have limited guesses
when guesses end...print game over
"""
print("\n\nThis is a GAME\n\nYou've to guess a number\nIt is ranged b/w 50 to 100")
num=78
i=10
while(True):
    a=int(input("Enter your guess\n"))
    if(a<num):
        print("Bigger")
        i=i-1
        print("You have",i,"left")
        if(i==0):
            print("GAME OVER")
            break
        else:
            continue
    if(a>num):
        print("Smaller")
        print("You have",i,"left")
        if(i==0):
            print("----------------GAME OVER----------------")
            break
        else:
            continue
    else:
        print("You won the game")
        print("you completed the game in",11-i,"guesses")
        break


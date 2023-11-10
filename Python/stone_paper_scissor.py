import random
print("\n\n\nYou have to play this game ten times. At last we will show you who won...\nEnter your choice\n's' for stone\n'p' for paper\n'sc' for scissors\n")
a=0
spr=["stone","paper","scissor"]
comp_points=0
user_points=0
while(a<=10):
    comp_choice=random.choice(spr)
    user_choice=input("Your Choice\n")
    # user wins
    if(user_choice=='s' and comp_choice=="scissor"):
        print("You won.  Computer's choice-",comp_choice)
        user_points+=1
        a+=1
        continue
    elif(user_choice=='p' and comp_choice=="stone"):
        print("You won.  Computer's choice-",comp_choice)
        user_points+=1
        a+=1
        continue
    elif(user_choice=='sc' and comp_choice=="paper"):
        print("You won.  Computer's choice-",comp_choice)
        user_points+=1
        a+=1
        continue
    #computer wins
    elif(user_choice=='sc' and comp_choice=="stone"):
        print("You loose.  Computer's choice-",comp_choice)
        comp_points+=1
        a+=1
        continue
    elif(user_choice=='s' and comp_choice=="paper"):
        print("You loose.  Computer's choice-",comp_choice)
        comp_points+=1
        a+=1
        continue
    elif(user_choice=='p' and comp_choice=="sc"):
        print("You loose.  Computer's choice-",comp_choice)
        comp_points+=1
        a+=1
        continue
    #Ties
    elif(user_choice=='sc' and comp_choice=="scissors"):
        print("TIE.  Computer's choice-",comp_choice)
        a+=1
        continue
    elif(user_choice=='s' and comp_choice=="stone"):
        print("TIE.  Computer's choice-",comp_choice)
        a+=1
        continue
    elif(user_choice=='p' and comp_choice=="paper"):
        print("TIE.  Computer's choice-",comp_choice)
        a+=1
        continue
if(comp_points>user_points):
    print("\n\n\nYOU LOOSE\ncomputer points-",comp_points,"\nYour points-",user_points)
elif(comp_points<user_points):
    print("\n\n\nYOU WON\ncomputer points-",comp_points,"\nYour points-",user_points)
else:
    print("\n\n\nIts a TIE \ncomputer points-",comp_points,"\nYour points-",user_points)
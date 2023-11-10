import random
print('----THE PERFECT GUESS----')
print("Guess the number between 1 and 100")
while True:
    i=1
    num=random.randint(1,100)
    while True:
        user_num=int(input("Enter: "))
        if user_num==num:
            print('Perfect! You guessed it!')
            print(f'You guessed it in {i} tries.')
            break
        elif user_num>num:
            print('Lower number please...')
            i+=1
            continue
        elif user_num<num:
            print('Higher number please...')
            i+=1
            continue
    again=input("Do you want to play again?(Y/N) ")
    if again=='Y':
        continue
    else:
        break    
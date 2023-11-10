import random

print("-----Stone Paper Scissors-----\n-----Press '69' any time to exit-----")
def with_comp():
    opt=['r','p','s']
    while True:
        comp_choice=random.choice(opt)
        user_choice=input("Rock(r) Paper(p) Scissors(s): ")
        if user_choice=='69':
            break

        elif comp_choice==user_choice:
            print('Draw!')
            continue
        
        elif comp_choice=='r' and user_choice=='p':
            print('You Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')            
            continue
        elif comp_choice=='r' and user_choice=='s':
            print('Computer Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')
            continue
        
        elif comp_choice=='p' and user_choice=='r':
            print('Computer Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')
            continue
        elif comp_choice=='p' and user_choice=='s':
            print('You Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')
            continue

        elif comp_choice=='s' and user_choice=='r':
            print('You Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')
            continue
        elif comp_choice=='s' and user_choice=='p':
            print('Computer Win!')
            print(f'Computer\'s choice: {comp_choice}\n\n')
            continue

def two_player():
    while True:
        user1_choice=input("Player 1:Rock(r) Paper(p) Scissors(s): ")
        user2_choice=input("Player 2:Rock(r) Paper(p) Scissors(s): ")

        if user1_choice=='69' or user2_choice=='69':
            break
        if user2_choice==user1_choice:
            print('Draw!')
            continue
        
        elif user2_choice=='r' and user1_choice=='p':
            print('Player 1 Win!\n\n')
            continue
        elif user2_choice=='r' and user1_choice=='s':
            print('Player 2 Win!\n\n')
            continue
        
        elif user2_choice=='p' and user1_choice=='r':
            print('Player 2 Win!\n\n')
            continue
        elif user2_choice=='p' and user1_choice=='s':
            print('Player 1 Win!\n\n')
            continue

        elif user2_choice=='s' and user1_choice=='r':
            print('Player 1 Win!\n\n')
            continue
        elif user2_choice=='s' and user1_choice=='p':
            print('Player 2 Win!\n\n')
            continue

choice=int(input("How do you wanna play?\nPress 1:With Computer.\nPress 2:Two Player Game."))
if choice==1:
    with_comp()
elif choice==2:
    two_player()
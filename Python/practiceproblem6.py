import random
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

random_num = random.randint(start,end)
print(f"Guess the Number....It is b/w {start} and {end}")
player1guess = 1
player2guess = 1
print("\n\n-----Player 1-----")
while True:
    user1 = int(input("Your guess:"))
    if user1 > random_num:
        print(f"Wrong guess....guess a smaller one")
        player1guess += 1
        continue
    elif user1 < random_num:
        print(f"Wrong guess....guess a larger one")
        player1guess += 1
        continue
    else:
        print(f"Correct")
    break
print("\n\n-----Player 2-----")
while True:
    user1 = int(input("Your guess:"))
    if user1 > random_num:
        print(f"Wrong guess....guess a smaller one")
        player2guess += 1
        continue
    elif user1 < random_num:
        print(f"Wrong guess....guess a larger one")
        player2guess += 1
        continue
    else:
        print(f"Correct")
        break
if player1guess > player2guess:
    print(f"\nPlayer 2 wins\nGuesses:{player2guess}")
elif player1guess < player2guess:
    print(f"\nPlayer 1 wins\nGuesses:{player1guess}")
else:
    print("It's a tie")
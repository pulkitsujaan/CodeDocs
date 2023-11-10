import random


def guess(start, end):
    guesses = 1
    random_num = random.randint(start, end)
    print(f"Guess the Number....It is b/w {start} and {end}")
    while True:
        user1 = int(input("Your guess:"))
        if user1 > random_num:
            print(f"Wrong guess....guess a smaller one")
            guesses += 1
            continue
        elif user1 < random_num:
            print(f"Wrong guess....guess a larger one")
            guesses += 1
            continue
        else:
            print(f"Correct")
        break
    return guesses


start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

print("\n\n-----Player 1 turn-----\n")
player1guess = guess(start, end)
print("\n\n-----Player 2 turn-----\n")
player2guess = guess(start, end)
if player1guess > player2guess:
    print(
        f"\n------Player 2 wins------\nPlayer 2 Guesses:{player2guess}\nPlayer 1 Guesses:{player1guess}")
elif player1guess < player2guess:
    print(
        f"\n------Player 1 wins------\nPlayer 1 Guesses:{player1guess}\nPlayer 2 Guesses:{player2guess}")
else:
    print("It's a tie")

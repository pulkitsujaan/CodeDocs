import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')


def game():
    score=int(input("Enter your high score: "))
    return score

while True:
    with open('highScore.txt','r') as f:
        current=f.read()
    print(f'\nCurrent Score:{current}')
    high_score=game()
    if current=='':
        with open('highScore.txt','w') as f:
            f.write(str(high_score))
    elif high_score>int(current):
        with open('highScore.txt','w') as f:
            f.write(str(high_score))

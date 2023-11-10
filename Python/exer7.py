from pygame import mixer
from datetime import datetime
import time
def music(musicfile,stoppingWord):
    mixer.init()
    mixer.music.load(musicfile)
    mixer.music.play(-1)
    while True:
        a=input()
        if a==stoppingWord:
            mixer.music.stop()
            break
def log(message):
    with open("logforhealthyprogrammer.txt","a") as f:
        f.write(f"{message}:{datetime.now()}\n")
watertime=5
eyestime=10
exertime=20
init_water=time()
init_eyes=time()
init_exer=time()
while True:
    if time()-init_water>=watertime:
        print("Time to drink water. Enter 'done' to stop the alarm")
        music("drink water.mp3",'done')
        log("Drank water at")
        init_water=time()
    if exertime<=time()-init_exer:
        print("Time to do some Exercise. Enter 'done' to stop the alarm")
        music("exer.mp3",'done')
        log("Did exericse at")
        init_exer=time()
    if eyestime<=time()-init_eyes:
        print("Time to relax eyes. Enter 'done' to stop the alarm")
        music("eye.mp3",'done')
        log("eyes relaxed at")
        init_eyes=time()
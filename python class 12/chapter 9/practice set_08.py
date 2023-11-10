import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

with open('this.txt') as f:
    thiscont=f.read()
with open('that.txt') as w:
    thatcont=w.read()

if thiscont==thatcont:
    print("Equal!")
else:
    print("Race")
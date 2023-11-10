import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

cuss=['donkey','to','is']
with open('textFor4.txt','r') as f:
    text=f.read()
with open('textFor4.txt','w') as f:
    for i in cuss:
        text=text.replace(i,'######')
    f.write(text)
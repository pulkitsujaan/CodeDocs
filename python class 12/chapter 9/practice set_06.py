import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')


logdata=True
i=1
with open('logfilesample.txt','r') as f:
    while logdata:
        logdata=f.readline()
        if 'python' in logdata.lower():
            print
            print(f"Contains Python in line {i}")
        i+=1
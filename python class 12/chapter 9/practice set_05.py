import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')



with open('logfilesample.txt','r') as f:
    logdata=f.read()
    if 'python' in logdata:
        print("Contains Python!")
    else:
        print("Don't have python!")
import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

with open('this.txt') as f:
    copy=f.read()
with open('that.txt','w') as w:
    w.write(copy)
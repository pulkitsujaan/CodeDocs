'''with statement'''
import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

with open('sample.txt', 'a') as f:
    f.write('xxx')

with open('another.txt', 'w') as f:
    f.write('brrrrrrr')
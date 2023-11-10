'''rename file'''
import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')


with open('delete.txt') as f:
    cont=f.read()
with open('renamed_by_python.txt','w') as u:
    u.write(cont)

os.remove('delete.txt')
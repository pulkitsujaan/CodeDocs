'''file I/O'''
import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')



f=open('sample.txt','r')#'r' is read mode

# data=f.read()
# data=f.read(5)#read first 5 characters of file 
# data=f.readline()#read a line, you can run it multiple times

# print(data)
f.close()
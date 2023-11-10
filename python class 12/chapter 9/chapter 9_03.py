import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

# f=open('another.txt','a')#append mode adds data to the file
# f.write("Hey! It's me peter parker \n")

f=open('another.txt','w')# write mode first removes everything, then writes into it.
f.write("Hey! It's me!")

f.close()

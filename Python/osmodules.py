import os

# print(dir(os))#functions in os module

# print(os.getcwd())#current working directory
# os.chdir("C://")#change directory
# print(os.getcwd())#print changed directory
# f=open("pulkit.txt")#this will print an error, because you've changed the directory

# a=os.listdir()#files present in this folder will be stored as a list
# for items in a:
#     print(items)

# os.mkdir("This")#make new folder in cwd
# os.makedirs("This/that")#make folder in new folder

# os.rename("PulkitBhai.txt","pulkit.txt")

# print(os.environ.get('path'))#get environment variables
# print(os.path.join("C:/","pulkit.txt"))#to join path with some minor mistakes

# print(os.path.exists("C://"))#exists or not?

# print(os.path.isdir("C://"))#directory exits or not
# print(os.path.isfile("pulkit.txt"))#file exists or not

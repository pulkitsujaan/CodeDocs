import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9')

'''read content of poems .txt and find whether it contains "twinkle" or not'''

with open('poems.txt','r') as f:
    content=f.read()
    print(content)
    if 'twinkle' in content:
        print("Yes! It is little stars")
    else:
        print('No shit Harrington!')
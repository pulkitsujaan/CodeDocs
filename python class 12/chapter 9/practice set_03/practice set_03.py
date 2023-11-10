import os
os.chdir(r'D:\Code Docs\python class 12\chapter 9\practice set_03')

for i in range(2,21):
    with open(f'tableof{i}', 'w') as t:
        for num in range(1,11):
            t.write(str(i*num)+'\n')
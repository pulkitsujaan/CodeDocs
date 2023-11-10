import random


def faultymulti(num):
    fault = random.randint(0,9)
    table = []
    for i in range(1, 11):
        table.append(num*i)
    table[random.randint(0,11)] = fault
    return table


def isCorrect(table, num):
    for i in range(1,11):
        if table[i-1] != i*num:
            return i-1
        
    return None
number=int(input("Enter number to find multiplication table:"))
table=faultymulti(number)
index=isCorrect(table,number)
print(f"Table:\n{table}")
print(f"wrong index:{index}")
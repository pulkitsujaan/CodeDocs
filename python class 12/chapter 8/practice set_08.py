def table(num):
    tab=[]
    for i in range(1,11):
        tab.append(num*i)
    return tab

value=int(input("Enter the number: "))
multi=table(value)
for i in multi:
    print(i) 
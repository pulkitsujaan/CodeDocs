num=int(input("Enter number: "))
table=[]
for i in range(num,(num*10)+1,num):
    table.append(i)
table.reverse()
for i in range(0,len(table)):
    print(f'{num} X {len(table)-i} = {num*(len(table)-i)}')
'''sum of first n natural numbers'''
num=int(input("Enter the number till you want to find the sum:"))
i=0
sum=0
while i<=num:
    sum+=i
    i+=1
print(f'Sum: {sum}')
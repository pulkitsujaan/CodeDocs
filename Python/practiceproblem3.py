a=[66,78,93,67457,654,4356,685,234,643,35]

#1st method
a.reverse()
print(a)
a.reverse()

# 2nd method
print(a[::-1])

# 3rd method
for items in range(len(a)//2):
    a[items],a[len(a)-items-1]=a[len(a)-items-1],a[items]
print(a)
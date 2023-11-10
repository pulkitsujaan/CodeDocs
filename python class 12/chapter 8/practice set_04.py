def sum_rec(n):
    if n==0:
        return 0
    else:
        return n+sum_rec(n-1)
    
nsum=sum_rec(10)
print(nsum)
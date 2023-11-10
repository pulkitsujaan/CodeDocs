'''Functions'''
def percent(a):
    per=((a[0]+a[1]+a[2]+a[3]+a[4])/400)*100
    return per

marks=[10,20,30,50,56]
perc1=percent(marks)
print(perc1)

marks2=[80,80,70,79,76]
perc2=percent(marks2)
print(perc2)
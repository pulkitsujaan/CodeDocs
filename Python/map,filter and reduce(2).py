#normal fuction to typecast to int
# lst=["56","67","35","214"]
# for i in range(len(lst)):
#     lst[i]=int(lst[i])
# print(lst[3]+6)
"""MAP"""
#map function
# a=list(map(int, lst))
# print(a[2]+5)


#code to print the square and cube of given range of given range
# def cube(a):
    # return a*a*a
# def square(a):
    # return a*a
# lst2=[square,cube]
# for i in range(input("Enter range for square and cubes\n")+1):
    # var=list(map(lambda x:x(i), lst2))
    # print(var)
"""FILTER"""
# lst3=[1,2,3,4,5,6,7,8,9]
# filt_list=list(filter(lambda x:x<5, lst3))
# print(filt_list)

"""REDUCE"""
from functools import reduce
lst4=[1,2,3,4,5,6,7,8,9,10]
num=reduce(lambda x,y:x+y, lst4)
print(num)
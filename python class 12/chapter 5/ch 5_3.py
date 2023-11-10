'''Sets'''
# #Sets are the organized collection of non-repetative items
# set1={1,3,4,6,7,5,2,3}
# print(set1)

'''IMPORTANT'''
'''
a={} creates empty dictionary
b=set() creates empty set

'''

b=set()
# print(type(b))
b.add(3)
b.add("Yes")
b.add((1,2,4,5,6))
# print(b)
# b.add([1,2,3])#Lists and dictionaries cannot be added to a set

# print(len(b))
# b.remove(3)#Removes 3, if not present...throws Key error
# b.pop()#removes last element from set
# print(b)
# b.clear()#empties the set

# set2={2,3,4,5,6}
# set3={1,2,3,4}
# print(set2.intersection(set3))#intersection of two sets
# print(set2.union(set3))#union of two sets
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - Process of using the first 2 points

"""
#int object is not iterable
#generators are iterable objects but didn't iterate always
#we can iterate a generator only once
def gen(i):
    for n in range(i):
        yield n
g="Pulkit"
for i in g:
    print (i)
# ob=iter(g)
# print(ob.__next__())
# print(ob.__next__())
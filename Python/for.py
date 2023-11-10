"""

syntax:
for varName in data_type:
    command

"""

list1=[77,55,89,2,4,6]
list0=[["one", 77],["two", 77], ["Three",88]]
dict1=dict(list0)

for item in dict1.items():
    if 77 in list1:
        print(item)

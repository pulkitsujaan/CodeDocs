"""
print some list items using for loop that are numbers and are bigger than 6
"""

list1=["harry", "voldemort", "dumbledore", 100, 112, 102, 93453456,87545135,435643564]
for items in list1:
    if str(items).isnumeric() and items>6:
        print(items)

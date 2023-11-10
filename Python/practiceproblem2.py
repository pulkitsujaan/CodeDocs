apples=int(input("Enter the no. of apples:"))
rangeStart=int(input("Enter the starting of a range:"))
rangeEnd=int(input("Enter the end of range:"))

if rangeStart==rangeEnd:
    print("This is not a range....bcz same numbers are given...")
    exit()

for items in range(rangeStart,rangeEnd+1):
    if apples%items==0:
        print(f"{items} is a divisor of {apples}")
    else:
        print(f"{items} is not a divisor of {apples}")
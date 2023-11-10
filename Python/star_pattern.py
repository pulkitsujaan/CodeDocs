a=int(input("Enter number of rows"))+1
ask=input("Enter 0 for assending and 1 for descending\n")
assend_decend=bool(ask)
if (assend_decend==0):
    for i in range(a):
        print("*"*i)
    print()
else:
    for i in range(a,0,-1):
        print("*"*i)
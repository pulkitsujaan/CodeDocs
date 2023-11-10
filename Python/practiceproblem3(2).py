size=int(input("enter the size of list:"))
lst=[]
for i in range(size):
    lst.append(int(input("Enter list element:")))
# lst.sort()
print(f"\nYour list is {lst}\n")

reverse1=lst[:]
reverse1.reverse()
print(f"First reverse:{reverse1}")

reverse2=lst[:]
print(f"Second reverse:{reverse2[::-1]}")

reverse3=lst[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"Third reverse:{reverse3}")

if reverse1==reverse2==reverse3:
    print("\nAll three lists are equally reversed...")
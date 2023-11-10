num=int(input("Enter a number: "))
# for i in range(2,num):
#     if i==num-1:
#         print("Number is prime.")
#         break
#     if num%i!=0:
#         continue
#     else:
#         print("Number is not prime.")
#         break


prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print("Number is prime.")
else:
    print("Number is not prime.")
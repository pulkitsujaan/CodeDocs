# #without recursion
# def factorial_iter(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact

# print(factorial_iter(4))
# print(factorial_iter(10))
# print(factorial_iter(0))

# # with recursion
# n! = n * (n-1)!
# def factorial_recur(n):
#     if n==0 or n==1:
#         return 1
#     else:
#        return n*factorial_recur(n-1)

# print(factorial_recur(10))
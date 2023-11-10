# # using list with while loops
# passwords=['ja123ne','thor069','anthonyh.stark007']
# secured_pass=[]
# while passwords:
#     password=passwords.pop()
#     print(f"Verifying password {password}....")
#     secured_pass.append(password)
# print("\nPasswords verified:")
# for passes in secured_pass:
#     print(passes)

# #Using while loop with dictionaries----favorite food
# print('----poll----')
# responses={}
# while True:
#     name=input("What is your name? ")
#     response=input("What is your favorite food item? ")
#     responses[name]=response
#     test=input("Would you like to let another person to take this poll?(yes/no) ")
#     if test=='no':
#         break
# #results
# print('\n----polling results----')
# for name,food in responses.items():
#     print(f"{name}'s favorite food is {food}")
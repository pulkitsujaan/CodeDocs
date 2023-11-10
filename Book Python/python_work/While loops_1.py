# number=1
# while number<=10:
#     print(number)
#     number+=1

print("Send me a message, I will send it back to you\n Send 'quit' to exit")
# message=''
# while message!='quit':
#     message=input("message: ")
#     if message!='quit':
#         print(message)

# # Flags help us to create multiple exits in a while loop, here, 'active' is the flag
# active=True
# while active:
#     message=input("message: ")
#     if message=='quit':
#         active=False
#     else:
#         print(message)

# # break
while True:
    message=input("message: ")
    if message=='quit':
        break
    else:
        print(message)
message=input("Enter a message:\n")
if ("make a lot of money" in message) or ("buy now" in message) or ('subscribe this' in message) or ('click this' in message):
    print("This is a spam message!!")
else:
    print("This message is completely fine!")
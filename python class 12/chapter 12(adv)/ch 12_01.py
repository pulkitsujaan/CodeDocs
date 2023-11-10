print("Press 'q' anytime to exit...")
while True:
    user=input("Enter a number: ")
    if user=='q':
        break

    try: # try and except help us to handle an error, without stopping the flow of code
        a=int(user)
        if a>10:
            print("You entered a number greater than 10")
    except Exception as e:
        print(e)

print("The end!")   
try:
    a=input('Enter a number: ')
    div=1/a
except ValueError as e:#You can handle different types of errors too
    print("Enter a valid value")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")

print("Bye")
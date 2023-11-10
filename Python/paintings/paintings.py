print("\nDo You want to add or show paintings?(a/sh)")
while True:
    choice = input("\nChoice:")
    if choice == "a":
        with open("paintings.txt", 'a') as f:
            data = input("Enter name of painting: ")
            f.write(f"{data}\n")
            print("painting added")
    else:
        with open("paintings.txt") as f:
            print(f.read())
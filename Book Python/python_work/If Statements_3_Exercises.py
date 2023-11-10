# # Pg-84
# alien_colour = ["Green", "Blue", "Purple", "Skin"]
# for items in alien_colour:
#     if items == "Pink":
#         print("You just earned 5 Points!!")
#     else:
#         print()

# pg-89
# usernames = ["jordan", "pulkit", "tiger", "@admin", "rowan", "leech"]
# for user in usernames:
#     if user == "@admin":
#         print("Hello Admin!! Would you like to see a status report?")
#     else:
#         print(f"Hello {user}!! Welcome back to the group")

# usernames = []
# if usernames:
#     for user in usernames:
#         if user == "@admin":
#             print("Hello Admin!! Would you like to see a status report?")
#         else:
#             print(f"Hello {user}!! Welcome back to the group")
# else:
#     print("We've to find some users!")

numbers = [i for i in range(1, 10)]
for number in numbers:
    if number == 1:
        number = "1st"
        print(number)
    elif number == 2:
        number = "2nd"
        print(number)
    elif number == 3:
        number = "3rd"
        print(number)
    else:
        number = f"{number}th"
        print(number)

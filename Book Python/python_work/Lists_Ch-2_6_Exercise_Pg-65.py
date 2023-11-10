# # Exercises 1
dishes=["Chhole Bhature","Pizza","Chicken curry","Gol Gappe","Tikki"]
# print(f"The first three items in the list are: {dishes[:3]}")
# print(f"Three items from the middle of the list are: {dishes[2:5]}")
# print(f"The last three items in the list are: {dishes[-3:]}")

# Exrcise 2
dishes2=dishes[:]
dishes.append("Paneer")
dishes2.append("Namkeen Chawal")
# print(f"My dishes:\n{dishes}")
# print(f"My dishes 2:\n{dishes2}")

#Exercise 3
for item in dishes:
    print(item)
print("\n")
for item in dishes2:
    print(item)
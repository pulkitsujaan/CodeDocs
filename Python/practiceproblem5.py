# pallindrome is a number which when reversed remains constant
def is_pallindrome(num):
    return str(num) == str(num)[::-1]


def pallindrome(num):
    num += 1
    while not is_pallindrome(num):
        num += 1
    return num


num_of_items = int(
    input("Enter the no. of items for you want to add in your list:"))

print("\n")

numbers_test = []
for items in range(num_of_items):
    items = int(input("Enter number:"))
    numbers_test.append(items)


print("\n")

pallindrome_list = []
for items in numbers_test:
    if items > 10:
        pallindrome_list.append(pallindrome(items))
    else:
        pallindrome_list.append(items)
print(f"Actual List:\n{numbers_test}")
print(f"\nPallindromified list:\n{pallindrome_list}")

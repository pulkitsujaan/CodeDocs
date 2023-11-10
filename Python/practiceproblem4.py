# pallindrome is a number which when reversed remains constant
def is_pallindrome(num):
    return str(num) == str(num)[::-1]


def pallindrome(num):
    num += 1
    while not is_pallindrome(num):
        num += 1
    return num


test_cases = int(
    input("Enter the no. of cases for you want to test the pallindrome:"))

print("\n")

numbers_test = []
for items in range(test_cases):
    items = int(input("Enter number:"))
    numbers_test.append(items)

# reversed_list=[]
# for items in numbers_test:
#     reversed_list.append(items[::-1])

print("\n")

for items in range(test_cases):
    print(
        f"Next pallindrome for {numbers_test[items]} is {pallindrome(numbers_test[items])}")

"""comprehensions""" 
#comprehensions are of types list, dict, sets, generators


#printing a list by normal method
# for i in range(1, 20):
#     if i%2==0:
#         lst1.append(i)


#list comprehension
# lst1=[i for i in range(20) if i%2==0]
# print(lst1)


#dictonary comprehension
# dict1={key:f"value {key}" for key in range(5)}
# print(dict1)

#reversing dictionary through comprehension
# dict2={value:key for key,value in dict1.items()}
# print(dict2)


#set comprehension
# langs=[lang for lang in ["Java","Python","C","C++","C#","Java","Java","Java","Java"]]
# print(type(langs))

#generator comprehension
# evenNums=(i for i in range(5) if i%2==0)
# print(evenNums.__next__())
# print(evenNums.__next__())
# for a in evenNums:
#     print(a)
# print("After")
# for a in evenNums:
#     print(a)
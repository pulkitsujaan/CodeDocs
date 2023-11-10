# user={
#     'first_name':'Pulkit',
#     'last_name':'Sujaan',
#     'username':'pulkitsujaan'
# }
# #Looping through all the key value pairs of dictionaries
# for key,value in user.items():
#     print(f"\nkey:{key}")
#     print(f"value:{value}")

#Looping with keys only
# for key in user:
#     print(key)

favorite_number={
    "Pulkit":69,
    "Dhruv":1,
    "Ayushi":10,
    "gunjan":100,
    "Dad":80
}
# family=["dad","dhruv","pulkit"]
# for name in favorite_number:
#     name=name.lower()
#     print(name.title())
#     if name in family:
#         print(f"\t{name.title()}, Hello!") 

# rivers={
#     "Nile":"Egypt",
#     "Ganga":"India",
#     "Indus":"Nepal",
#     "Amazon":"Africa"
# }
# for river, country in rivers.items():
#     print(f"The {river} runs through {country}")

# print("\nRivers included:")
# for river in rivers:
#     print(river)

# print("\nCountries included:")
# for Country in rivers.values():
#     print(Country)

friends=["dhruv","aditi","ashutosh","yash","dad","ayushi"]
for name in favorite_number:
    name=name.lower()
    if name in friends:
        print(f"Thank You {name.title()} for telling me your favorite number.")
    else:
        print(f"Please tell me your favorite number {name.title()}")
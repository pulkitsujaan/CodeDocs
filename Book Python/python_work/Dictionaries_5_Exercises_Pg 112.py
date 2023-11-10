# exercise 6-7
person1={
    "first_name":"pulkit",
    "last_name":"sujaan",
    "age":15,
    "city":"meerut",
}
person2={
    'first_name':'ayushi',
    'last_name':'sujaan',
    'age':18,
    'city':'meerut'
}
person3={
    'first_name':'gunjan',
    'last_name':'',
    'age':17,
    'city':'meerut'
}
siblings=[person1,person2,person3]
# for sibling in siblings:
#     print(sibling)

# exercise 6-8
pet1={
    'name':'sheero',
    'age':5,
    'owner':'shinchan'
}
pet2={
    'name':'bruno',
    'age':7,
    'owner':'chad'
}
pet3={
    'name':'sexa',
    'age':12,
    'owner':'crood'
}
pets=[pet1,pet2,pet3]
# for pet in pets:
#     print(pet)

favorite_places={
    'pulkit':['New York','Texas','India'],
    'gunjan':['India','USA','Taliban'],
    'ayushi':['Afghanistan','Pakistan','Nepal']
}
for name,place in favorite_places.items():
    print(f'Name : {name}')
    print(f'Favorite Places:\n\t{place}')
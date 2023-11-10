#Dictionary in a list
user_0={"name":"Pulkit", "Class":10}
user_1={"name":"Gunjan","Class":10}
user_2={"name":"Ayushi","Class":10}

users=[user_0,user_1,user_2]
# for user in users:
#     print(user)


# List in a Dictionary
pizza={
    "base":"Thick",
    "Topping":["Pepperoni","Chilli flake"]
}
# print(f"You ordered a {pizza['base']}-base Pizza")
# print(f"Toppings added:\n\t{pizza['Topping']}")

# Dictionary in a Dictionary
dict_dict={
    'sujaan2708':{
        'first_name':'pulkit',
        'last_name':'sujaan',
        'hobby':'Coding'
    },
    'asujaan3':{
        'first_name':'ayushi',
        'last_name':'sujaan',
        'hobby':'badtameezi'
    },
}

for user,info in dict_dict.items():
    print(f"Username:{user}")
    full_name=f"{info['first_name'].title()} {info['last_name'].title()}"
    hobby=info['hobby']

    print(f'\t Full Name: {full_name}')
    print(f'\t Hobby: {hobby}')
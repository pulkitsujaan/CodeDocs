# def proper_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         full_name=f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name=f'{first_name} {last_name}'
#     return full_name.title()
# print(proper_name(first_name='pulkit',last_name='sujaan'))

# # Returning a Dictionary
# def proper_name(first_name,last_name,age=None):
#     full_name={
#         'first':first_name,
#         'last':last_name
#     }
#     if age:
#         full_name['age']=age
#     return full_name
# print(proper_name(first_name='pulkit',last_name='sujaan',age=15))

# Using While loop with functions
def proper_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f'{first_name} {last_name}'
    return full_name.title()
while True:
    print('Enter "q" to quit')
    f_name=input("Enter first name: ")
    if f_name=='q':
        break
    l_name=input('Enter last name: ')
    if l_name=='q':
        break
    full_name=proper_name(first_name=f_name,last_name=l_name)
    print(f'\nHello {full_name}\n')
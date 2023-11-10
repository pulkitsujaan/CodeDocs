# def say_hello(users):
#     for user in users:
#         print(f'Hello, {user.title()}!')
# users=['pulkit','gunjan','ayushi']
# say_hello(users)

# #Pizzas Re-written
# def order_pizza(Orders,completed):
#     while Orders:
#         order=Orders.pop()
#         print(f'Making {order} Pizza...')
#         completed.append(order)

# def print_completed(completed_pizza):
#     print('\n')
#     for pizza in completed_pizza:
#         print(f'Made {pizza} Pizza')


# ordered_pizza=['margehretta','peproni','cheese burst']
# completed_pizza=[]

# order_pizza(ordered_pizza,completed_pizza)
# print_completed(completed_pizza)

'''----------------------------------------------'''

# # Exercises Pg-146
# # Exercise 8-9
# def show_messages(message_list):
#     for message in message_list:
#         print(message)
# messages=['hey,there','Ohh God!','I am Iron Man','Love you 3000']
# show_messages(message_list=messages)

# # Exercise 8-10
# sent_message=[]
# def show_messages(message_list):
#     while message_list:
#         message=message_list.pop()
#         print(message)
#         sent_message.append(message)
# messages=['hey,there','Ohh God!','I am Iron Man','Love you 3000']
# show_messages(message_list=messages)
# print(messages)
# print(sent_message)

# # Exercise 8-11
# sent_message=[]
# def show_messages(message_list):
#     while message_list:
#         message=message_list.pop()
#         print(message)
#         sent_message.append(message)
# messages=['hey,there','Ohh God!','I am Iron Man','Love you 3000']
# show_messages(messages[:])
# print(messages)
# print(sent_message)
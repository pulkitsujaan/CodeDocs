# #Exercise 7-8
# sandwich_orders=['chicken sandwich','pastrami','egg sandwich','seafood sandwich','pastrami','pastrami','roast beef sandwich','grilled cheese']
# completed_sandwiches=[]
# print("We have run out of pastrami sandwiches")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     print(f'I completed your {sandwich}')
#     completed_sandwiches.append(sandwich)
# print('\nSandwitches Completed:')
# for items in completed_sandwiches:
#     print(items)

# #Exercise 7-10
# polling=True #polling active
# fav_place={}
# print('----poll----')
# while polling:
#     name=input('What is your name? ')
#     place=input('If you could visit one place in the world, where would you go? ')
#     fav_place[name]=place
#     again=input('Would you like to let another person take the poll?(yes/no) ')
#     if again=='no':
#         polling=False
# print('----poll results----')
# for name,place in fav_place.items():
#     print(f'{name} would like to go to {place}')
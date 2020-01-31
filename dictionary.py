

# user_info=dict(name='Mako', age=35, cute=True)
# print(user_info)
#
# artist = {
#     "first": "Neil",
#     "last": "Young",
#     "age":"45"
#
# }
# full_name=artist['first']+" "+ artist['last']
# print(full_name)
# for value in artist.values():
#     print(value)
#     for key in artist.keys():
#         print('the key is {}'.format(key))
# for key,value in artist.items():
#     print('{} is the key and {} is the value'.format(key, value))
#     print(f'{key} is the key and {value} is the value')
# print('Neil' in artist.values())
#
#
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donation=0
# for value in donations.values():
#     total_donation=total_donation+value
#     print(total_donation)
# #methodes
# new_don=donations.copy()
# print(new_don)
# #fromkey
# user=dict.fromkeys(['name', 'age', 'city', 'email'], None)
# print(user)
# print(user.get('name'))

from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
print(food)

#DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# items=0
# if food in bakery_stock:
#     items=bakery_stock[food]
#     print(items)
# else:
#      print('we dont do that')
#
# ame_properties = ["current_score",
#                   "high_score", "number_of_lives",
#                   "items_in_inventory", "power_ups",
#                   "ammo", "enemies_on_screen",
#                   "enemy_kills", "enemy_kill_streaks", "minutes_played",
#                   "notifications", "achievements"]
# initial_game_state={}.fromkeys([*ame_properties], 0)
# print(initial_game_state)
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# bakery=dict.fromkeys([*bakery_stock],0)
# print(bakery)
# bakery.pop('toffee cookie')
# print(bakery)
# bakery_new={'pan au chocolat': 10}
# bakery_new.update(bakery_stock)
# print(bakery_new)
# new_line={'scone':23}
# new_line.update(bakery_stock)
# print(bakery_stock)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list=inventory.copy()
print(stock_list)





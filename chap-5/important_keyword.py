toppings = ['mushrooms', 'tomatos', 'olives', 'ham']

# the keyword 'in' allows you to check if a value exists in a list
if 'mushrooms' in toppings:
    print('Good choice!')
else:
    print('You sure?')

# it's also useful to know if an item is not in a list
banned_users = ['andrew', 'george', 'beth', 'marie']
user = 'sylvia'

if user not in banned_users:
    print(f"{user.title()}, you may post a response if you wish.")
# can copy a list based on slicing a list
my_fav_foods = ['burrito', 'pizza', 'pasta', 'roll','ice cream']
friend_fav_foods = my_fav_foods[:]

friend_fav_foods.append('chocolate')

print("My favorite foods are:")
print(my_fav_foods)

print("My friend's favorite foods are:")
print(friend_fav_foods)
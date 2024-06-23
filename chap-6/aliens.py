# dictionaries allow you to associate one value with another- eg: names with fav colors
alien0 = {'color': "green", 'points': 5}

print(alien0['color']) # green
print(alien0['points']) # 5

# it is comprised of 'key-value pairs' -> key can be used to access associated value
# eg: the key 'color' is used to access the value 'green'

# using keys:
new_points = alien0['points']
print(f"You shot down the alien! You get {new_points} points.")

# dictionaries are dynamic- can add new key-value pairs
alien0['x-position'] = 0
alien0['y-position'] = 25
print(alien0) # elements are in the order they're added, chronologically

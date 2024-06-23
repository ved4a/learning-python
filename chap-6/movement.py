# let’s track the position of an alien that can move at different speeds.
alien0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien0['x-position']}")

# move the alien to the right

# how far right should it be moved?
speed = alien0['speed']
if speed == 'slow':
    x_increment = 1
elif speed == 'medium':
    x_increment = 3
else:
    x_increment = 5

# the new position of the alien is initial + increment
alien0['x-position'] = alien0['x-position'] + x_increment
print(f"New position: {alien0['x-position']}")
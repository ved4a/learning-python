alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  this doesn't exist, so now what?

# can use the get() method to set a default value for a key if it does not exist
point_val = alien_0.get('points', 'No point value assigned')
print(point_val)

print(alien_0.get('color'))
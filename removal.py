# key-value pairs can be deleted by using 'del'- this is permanent, value cannot be stored
house = {'price': 'a lot', 'space': 'not enough', 'neighbors': 'sweet'}
print(house)

# let us delete the key-value pair associated with neighbors
del house['neighbors']
print(house)
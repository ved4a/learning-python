squares = [] # initialize an empty list
for value in range(1,11): # range 1 to 10
    squares.append(value ** 2) # append the squared value of whichever number is current assigned "value"
print(squares)

digits = list(range(10))
print(min(digits))
print(max(digits))
print(sum(digits))

# a list comprehension combines a for loop and appending elements to a list
cubes = [value ** 3 for value in range(6)]
print(cubes)
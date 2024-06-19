# to create an immutable list, create a tuple
dimensions = (200,50) # defining the tuple
print(dimensions[0]) # can be accessed the same way elements of a list are accessed

# if we try reassigning the value within the tuple:
# dimensions[0] = 250 -> TypeError: 'tuple' object does not support item assignment

# Tuples are characterized by their commas, so even if the tuple has only 1 element, it should contain a trailing comma as per standards. eg: tuple = (5,)

# a tuple can be looped through in the same way as a list can:
for dimension in dimensions:
    print(dimension)

# Even though a tuple can't be modified, it can be overwritten
print("Original dimensions:")
print(dimensions)

dimensions = (400,120)
print("New dimensions:")
print(dimensions)
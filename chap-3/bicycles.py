bicycles = ['mountain', 'bmx', 'hybrid', 'electronic', 'road']
print(bicycles) # will print with square brackets and quotes
print(bicycles[1]) # will only print value: bmx

print(bicycles[2].title()) # since the values are strings, can use methods on the elements of the list

print(bicycles[-1]) # this prints the last element of the list- useful when you don't know how long a list is
# -2, -3, and so on as indexes are used for the second-last, third-last, and consequent elements

# individual values from a list can be used as variables, eg:
message = f"My first bike was a {bicycles[1].upper()}."
print(message)
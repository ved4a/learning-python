# can generate a set of numbers using Python
for value in range(1,6): # this would start at 1 and end at 5
    print(value)

# or

for value in range(6): # this would start at 0 and end at 5
    print(value)

# there's a 'list' function that will allow saving the generated numbers in a list
numbers = list(range(1,6))
print(numbers)

# the 'step' value need not even be 1, eg:
even_numbers = list(range(2, 11, 2)) # start at 2, stop before 11, add 2 at a time
print(even_numbers)
# most lists used will be dynamic- constantly removing, adding, and changing elements
motorcycles = ['honda', 'yamaha', 'bajaj', 'royal enfield']
print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles) ; honda changed to ducati

# however, if you want to add and not replace an element:
motorcycles.append('ducati') # adds to the end of a list
print(motorcycles)
# this is also helpful to build lists, because can start with an empty list and keep appending values

# if you know the index of an element you want to delete, then:
del motorcycles[1]
print(motorcycles) # you can no longer access the value 'yamaha'

# however, if you want to use a value that should no longer be in the list, then:
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) # the value 'ducati' is in here

# 'pop' without an argument will simply remove the last element from a list. but if you put in an index as an argument, then the corresponding value will be removed
pop_bajaj = motorcycles.pop(1)
print(motorcycles) # now only contains 2 elements
print(pop_bajaj) # has the value 'bajaj'

motorcycles = ['honda', 'suzuki', 'royal enfield'] # bikes stored in chronological order
# last_owned = motorcycles.pop()
# print(f"The last bike I ever had was a {last_owned}.")

first_owned = motorcycles.pop(0)
print(f"The first bike I ever owned was a {first_owned.title()}.")

# when you want to delete an item from a list and not use that item in any way, use the 'del' statement; if you want to use an item as you remove it, use the pop() method

# if you know the value, but not the index, you can still delete stuff from a list
motorcycles = ['honda', 'suzuki', 'royal enfield', 'ducati', 'indian', 'ather']
motorcycles.remove('suzuki')
print(motorcycles)

# can also use the remove method if the value is stored in a variable
electric = 'ather'
motorcycles.remove(electric)
print(motorcycles)
print(f"I do not think {electric.title()} is for me, I don't need an electric bike.")

# The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed. 
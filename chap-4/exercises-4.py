# 4-1
pizzas = ['margherita', 'pepperoni', 'veggie', 'double cheese']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("If you couldn't tell, I really like pizza!")

# 4-2
pets = ['dog', 'cat', 'bird', 'fish']
for pet in pets:
    print(f"A {pet} would make a good pet.")
print('Honestly, anything would make a good pet!')

# 4-3
for value in range(1,21):
    print(value)

# 4-5
million = list(range(1,1000001))
print(min(million))
print(max(million))
print(sum(million))

# 4-6
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

# 4-7
threes = list(range(3,31,3))
for three in threes:
    print(three)

# 4-8 + 4-9
cubes = [value ** 3 for value in range(1,11)]
print(cubes)
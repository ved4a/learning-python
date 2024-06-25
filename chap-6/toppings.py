# it is sometimes more useful to put a dictionary in a list
pizza = {
    'crust': 'thin',
    'toppings': ['mushroom', 'tomatos','onion']
}

print(f"You ordered a {pizza['crust']}-crust pizza, with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
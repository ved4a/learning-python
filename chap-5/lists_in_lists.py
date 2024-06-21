# to make this easier, we can have one list of requested toppings, and one list of available toppings
available_toppings = ['olives', 'onion', 'tomato', 'ham', 'sausage', 'extra cheese', 'anchovies', 'capsicum', 'corn']

requested_toppings = ['olives', 'fries', 'ketchup', 'ham']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")
print("Your pizza is complete!")
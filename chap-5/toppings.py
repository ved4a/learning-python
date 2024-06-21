# imagine you want to give your consumer a live recount of all toppings on their pizza
# this can be done by utilizing a for loop

# requested_toppings = ['mushroom', 'ham', 'olives', 'onion']
requested_toppings = []

for topping in requested_toppings:
    print(f"Adding {topping}.")

print("\nYour pizza is complete!")

# however, what if you're out of olives? this will have to be conveyed to the customer
for topping in requested_toppings:
    if topping == 'olives':
        print(f"Sorry, we're out of {topping}.")
    else:
        print(f"Adding {topping}.")

print("\nYour pizza is complete!")

# what if the list of items is empty? must add a condition for that.
if requested_toppings:
    for topping in requested_toppings:
        if topping == 'olives':
            print(f"Sorry, we're out of {topping}.")
        else:
            print(f"Adding {topping}.")
        print("\nYour pizza is complete!")
else:
    print("Are you sure you want a plain pizza?")
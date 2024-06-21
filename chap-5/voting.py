age = 23

if age >= 18:
    print("You're old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("You're not old enough to vote yet.")
    print("Please register to vote when you are 18!")

# the if-elif-else chain
if age < 4:
    print("You are free to enter, have fun!")
elif age < 18:
# i had originally put age >= 4 and age < 18, but that is redundant because skipping the first condition already proves that age > 4
    print("That'll be a fee of 25 dollars. Thank you!")
else:
    print("40 dollars please. Have fun!")

# however, a simpler way of doing this would be:
if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age < 45: # can use multiple elif blocks
    price = 35
else:
    price = 40

print(f"That'll be {price} dollars, thanks!")

# the 'else' block is a catchall statement. in Python, it can be removed if the elif conditions are sufficient. thus, not having an 'else' block will make you confident that you've accounted for all cases
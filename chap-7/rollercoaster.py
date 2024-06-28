# the input() function parses everything as a string
# need to convert before using value

height = input("How tall are you, in inches? ")
print(height)

height = int(height) # the string '71' is now the number 71

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nSorry, you do not meet the height requirement.")
# looping through all entries in a list allow a repetitive, irritating task to be finished efficiently with only a few lines of code

# for every magician in the list of magicians, print the magician’s name.
magicians = ['houdini', 'elsa', 'peter pan', 'lisa from the simpsons'] # define list
# for magician in magicians: ; define for loops
#    print(magician) ; determine action

# essentially, each value in the list- as we progress through it- is assigned to the variable 'magician', which is how it is printed -> 'magician' can be replaced with anything, but it's good practice to have the singular form of the items in the list to name it

# can do more than just print value:
for magician in magicians:
    print(f"Wow, {magician.title()}, that was a great trick!")
    print(f"I can't wait to see what you do next, {magician.title()}.\n")

print("Thank you everyone, what a wonderful performance!") # this is a good way to summarize the operations completed on a dataset, because it will only run after the loop has ended

# Python uses indentation to determine how a line of code fits into the rest of a program. Thus, if an indentation was expected, but did not arrive, there will be "IndentationError: expected an indented block" in the terminal

# Similarly, indenting unnecessarily will also throw an error back: "IndentationError: unexpected indent"
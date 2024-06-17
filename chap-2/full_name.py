firstName = 'ada'
lastName = 'lovelace'
fullName = f"{firstName} {lastName}" # f-string, aka a "formatted string". similar to using ${} with backticks in javascript

#  print(f"Hello, {fullName.title()}!") - using f-string + method + variable
sayHello = f"Hello, {fullName.title()}!"
print(sayHello)

print('Python')
print("\tPython") # adds whitespace in the form of a tab

print('Languages: \nPython \nC and C++ \nJava \nRust') # adds a new line, just like C

print('Now \n\tlet\'s \tstack \nthese \n\tskills!') # combining tab and new line

# stripping whitespace
msg = "I love Python "
print(msg)

msg.rstrip() # if printed, the whitespace is stripped only temporarily. to make it permanent, reassign the variable
msg = msg.rstrip() # reassigning the variable
print(msg)

# rstrip removes whitespace from the right side of a string, whereas lstrip will remove it from the left. in order to prevent an additional requirement of text, simply use "strip" as a method. eg: msg.strip()
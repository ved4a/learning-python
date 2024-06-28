# the prompt should be clear, so that the user KNOWS what to enter. eg:
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# can also write a prompt longer than one line:
prompt = "If you tell us who you are, we can personalize messages for you."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
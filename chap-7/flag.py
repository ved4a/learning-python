# if there are multiple conditions that determine whether a program
# can stop or not, then to account for all of them in 1 while loop
# becomes difficult. as a result, having just 1 signal to the program
# which is boolean, can make the process easier. this is called a flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
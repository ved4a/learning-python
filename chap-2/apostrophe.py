msg = "Python is a high-level programming language"

# next_message = 'Although some may say it's still tough
# the above will return "SyntaxError: invalid syntax", because the apostrophe in "it's" is being interpreted as the end of the string. to fix this, use double quotes for the string, or escape the apostrophe with a backslash. eg:

revamped_msg = "Although some may say it's still tough"
renewed_msg = 'Although some may say it\'s a little hard to pick up'

print(msg)
print(revamped_msg)
print(renewed_msg)

# 2-3
name = "Edna Mode"
print(f"Hello, {name}, it's been a while!")

# 2-4
friend = "SaSHa"
print(friend.upper())
print(friend.lower())
print(friend.title())

# 2-5
print('Eren Yaeger once said, "If we kill the enemy...will we finally win?".')

# 2-6
famous_person = "Eren Yaeger"
message = '"If we kill the enemy...will we finally win?"'
print(f"{famous_person} once said: {message}.")

import this
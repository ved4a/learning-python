user = {
    'username': 'enfermi',
    'first': 'enrico',
    'last': 'fermi'
}

# print(user.get('username'))
for key, value in user.items(): # items method returns key-value pairs
# 'key' and 'value' can also be replaced w/ k, v- doesn't matter
    print(f"\nKey: {key}")
    print(f"Value: {value}")
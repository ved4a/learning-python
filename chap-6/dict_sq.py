# can nest a dictionary inside a dictionary. eg:
users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tFirst Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
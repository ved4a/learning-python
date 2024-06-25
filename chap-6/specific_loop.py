# looping through keys
languages_spoken = {
    'hitori': 'japanese',
    'nikita': 'russian',
    'meg': 'english',
    'kannan': 'tamil'
}

for name in languages_spoken.keys():
    print(name.title())

# however, for dictionaries, the key is actually the default value, so:
for name in languages_spoken:
    print(name.title()) # this gives the same output

# using lists and dictionaries in tandem:
friends = ['kannan', 'nikita']

for name in languages_spoken:
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = languages_spoken[name].title()
        print(f"\t{name.title()}, I see you speak {language}!")

# can also use keys method to check if key exists in dict or no
if 'krish' not in languages_spoken.keys():
    print('Krish, please take the poll!')

# can also loop through keys in a dictionary in alphabetical order:
for name in sorted(languages_spoken.keys()):
    print(f"{name.title()}, thanks for taking the poll!")
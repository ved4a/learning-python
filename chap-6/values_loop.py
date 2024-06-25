favorite_languages = {
    'jen': 'c#',
    'alex': 'python',
    'meg': 'java',
    'tyler': 'assembly',
    'eric': 'c#',
    'fonzi': 'python',
    'shrek': 'c#'
}

# looping through values in a dictionary
for language in favorite_languages.values(): # use values method
    print(language.title())

# however, for large dictionaries which may contain results of a poll, many
# values will be repeated. to prevent this overload, use sets:
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

# a set can be directly made like so: languages = {'python', 'JS', 'assembly'}
# it's basically a list with curly brackets lol
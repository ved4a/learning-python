# can make a dictionary of similar values- eg a poll asking what everyone's fav language is
favorite_languages = {
    'eric': "C#",
    'mark': 'javascript',
    'jen': 'python',
    'emily': 'rust'
}

language = favorite_languages['emily'].title()
print(f"Emily's favorite language is {language}.")
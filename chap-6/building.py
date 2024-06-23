# it's sometimes convenient/necessary to begin with an empty dictionary, and dynamically build it
game = {}

game['name'] = 'stardew valley'
game['creator'] = 'concernedape'
game['release'] = 2016
game['genre'] = 'farming simulator'

print(game)

# since dictionaries are dynamic, their values can be modified
print(f"I thought the genre of {game['name']} was a {game['genre'].title()}.")
game['genre'] = 'indie life simulator'
print(f"The genre of {game['name']} is actually an {game['genre'].title()}.")
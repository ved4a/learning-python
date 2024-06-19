players = ['steph', 'lebron', 'cp3', 'KD', 'luka', 'trey', 'giannis']

# we can work with parts of a list, instead of a whole list- known as a SLICE of a list
print(players[2:6]) # 3rd to 6th players' names

print(players[5:]) # names of 6th player onwards

print(players[:4]) # all names until 4th player (inclusive)

print(players[-3:]) # last 3 players' names

# can loop through a slice
print("Here are the first three players of my team:")
for player in players[:3]:
    print(player.title())
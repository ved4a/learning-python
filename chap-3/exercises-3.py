# 3-4
guest_list = ['Madonna', 'Clairo', 'Iron Man']
print(f"Hi {guest_list[0]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[1]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[2]}, I'm having a small party, I'd love for you to come.")

# 3-5
print(f"Unfortunately, {guest_list[1]} could not make it.")

guest_list[1] = 'Steve Jobs'

print(f"Hi {guest_list[0]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[1]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[2]}, I'm having a small party, I'd love for you to come.")

# 3-6
print(f"Hi everyone, I found a bigger table.")

guest_list.insert(0, 'Leonardo da Vinci')
guest_list.insert(2, 'Freddie Mercury')
guest_list.append('Britney Spears')

print(f"Hi {guest_list[0]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[1]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[2]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[3]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[4]}, I'm having a small party, I'd love for you to come.")
print(f"Hi {guest_list[5]}, I'm having a small party, I'd love for you to come.")

# 3-7
print(f"Hi everyone, I am very sorry but my dinner table did not arrive on time, I'll only be able to invite two people to dinner.")

removed_person_1 = guest_list.pop(5)
print(f"Hi {removed_person_1}, I'm sorry I couldn't invite you to dinner.")

removed_person_2 = guest_list.pop(2)
print(f"Hi {removed_person_2}, I'm sorry I couldn't invite you to dinner.")

removed_person_3 = guest_list.pop(3)
print(f"Hi {removed_person_3}, I'm sorry I couldn't invite you to dinner.")

removed_person_4 = guest_list.pop(0)
print(f"Hi {removed_person_4}, I'm sorry I couldn't invite you to dinner.")

print(f"Hello {guest_list[0]}, just messaging to let you know that you're still invited. Looking forward to seeing you there!")
print(f"Hello {guest_list[1]}, just messaging to let you know that you're still invited. Looking forward to seeing you there!")

del guest_list[0]
del guest_list[0]

print(guest_list)

# 3-8
locations = ['oslo', 'amsterdam', 'spain', 'maldives', 'sydney']
print(locations)

print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

names = ['ali', 'hassan', 'sina']
# print(names[0])
# print(names[1])
# print(names[2])
# -----------------------------------
# print(f"Hello MR.{names[0]}")
# print(f"Hello MR.{names[1]}")
# print(f"Hello MR.{names[2]}")
# -----------------------------------
cars = ['benz', 'tesla', 'BMW']
# print(f"{names[1]} is my best friend and he has lots of cars such as {cars[2]}")
# -----------------------------------
motorcycle = []
motorcycle.append('honda')
motorcycle.append('Bmw')
# -----------------------------------
popped_names = names.pop()
# print(names)
# print(popped_names)
# -----------------------------------
guests = ['maryam', 'zahra', 'mina']
# print(f"Hi {guests[0]} you are invited to my dinner party")
# print(f"Hi {guests[1]} you are invited to my dinner party")
# print(f"Hi {guests[2]} you are invited to my dinner party")
guests[1] = 'Taran'
# print(guests)
# print(f"Hi {guests[0]} you are invited to my dinner party")
# print(f"Hi {guests[1]} you are invited to my dinner party")
# print(f"Hi {guests[2]} you are invited to my dinner party")
guests.insert(0, 'mamad')
guests.insert(2, 'ali')
guests.append('hosein')
# print(guests)
# for guest in guests:
#     print(f"Hi {guest} you are invited to my party")
guest_popping = guests.pop()
print(f"sorry {guest_popping} I dont have enough space for maybe next time")
guest_popping = guests.pop()
print(f"sorry {guest_popping} I dont have enough space for maybe next time")
guest_popping = guests.pop()
print(f"sorry {guest_popping} I dont have enough space for maybe next time")
guest_popping = guests.pop()
print(f"sorry {guest_popping} I dont have enough space for maybe next time")
print(guests)
for guest in guests:
    print(f"Hi {guest} you are still invited to my party")
del guests[0]
print(guests)
del guests[0]
print(guests)

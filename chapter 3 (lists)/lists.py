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
# guest_popping = guests.pop()
# print(f"sorry {guest_popping} I dont have enough space for maybe next time")
# guest_popping = guests.pop()
# print(f"sorry {guest_popping} I dont have enough space for maybe next time")
# guest_popping = guests.pop()
# print(f"sorry {guest_popping} I dont have enough space for maybe next time")
# guest_popping = guests.pop()
# print(f"sorry {guest_popping} I dont have enough space for maybe next time")
# print(guests)
# for guest in guests:
#     print(f"Hi {guest} you are still invited to my party")
# del guests[0]
# print(guests)
# del guests[0]
# print(guests)
# -----------------------------------
# location = ['vancouver', 'rome', 'miami', 'newyork', 'shiraz']
# print(location)
# print(sorted(location))
# print(location)
# print(sorted(location, reverse=True))
# print(location)
# location.reverse()
# print(location)
# location.reverse()
# print(location)
# location.sort()
# print(location)
# location.sort(reverse=True)
# print(location)
# count_guests = len(guests)
# print(f"We have {count_guests} in our party")
# -----------------------------------
cities = ['tehran', 'chalus', 'bandarabbas']
countries = ['canada', 'iran', 'italy']
cities.sort()
countries.reverse()
len_cities = len(cities)
print(
    f"There are {len_cities} cities I would like to go there such as {cities[2]}, after that I will go {countries[0]} with my wife")

# test = 1000
# rating = 4.99
# is_published = False
# full_name = "farzin shams"
# print(type(rating))

# ---------------

# course = "python programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:4])
# print(course[0:])
# print(course[:4])
# print(course[:])

# ---------------

"""\ is escape character"""
# course = "python "programming"
"""it turns error if we want use " in the middle of sentense
we need to write code like this:"""
# course = 'python "programming'
"""or"""
# course = "python \"programming"
"""both these example is true"""
# \"    """show " in line"""
# \'    """show ' in line"""
# \\    """show \ in line"""
# \n    """next line"""

# ----------------

# first = "Farzin"
# last = "Shams"
# full = first + " " + last
# print(full)
"""or"""
# full = f"{first} {last}"
# print(full)

# ----------------

# course = "   python programming"
# print(course.upper()) """turns every thing to uppercase"""
# print(course.lower()) """turns every thing to lowercase"""
# print(course.title()) """turns to capitalize"""
# print(course.strip()) """remove white spaces"""
# print(course.find("pro")) """find the word and show the index of that"""
# print(course.replace("p", "j")) """replace second place to first place"""
# print("pro" in course) """show your answer in boolian"""
# print("swift" not in course) """show your answer in boolian"""

# ----------------

# print(round(2.9))
# print(abs(-2.9))
# import math
# print(math.ceil(5.2))
# print(math.copysign(3, -7))

# -----------------

# x = int(input("x: "))
# y = x + 1
# print(f"x:{x}, y:{y}")

# False = "", None, 0
"""all of these are show false"""

# -------QUIZ-------

# fruit = "apple"
# print(fruit[1:-1])

# print(10 % 1)

# print(bool("False"))

# ------------------

# temperature = 15

# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")

# ------------------

# age = 22

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

"""Lets type that in clean way"""

# age = 25
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# ----OR-----

# age = int(input("Enter your age: "))
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# -----------------

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# elif high_income and good_credit == False:
#     print("You have no credit")
# elif high_income == False and good_credit:
#     print("Your income is low")
# else:
#     print("Not eligible")

"""or"""

# high_income = True
# good_credit = True
# student = False

# if (high_income and good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# ---------------

# age = 22
# if age >= 18 and age < 65:
#     print("Eligible")

"""or"""

# if 18 <= age < 65:
#     print("Eligible")

"""Both of them has same result but the second one is cleaner (like math)"""

# ---------------

# for number in range(1, 10, 2):
#     print("Row", number, number * ".")

# ---------------

# for x in range(1):
#     for y in range(3):
#         print(f"({x},{y})")

# ---------------

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

"""or we can type this code in better way"""

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# ---------------

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")

# ------------------------------------------------


# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# greet()

# ---------------

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Farzin", "Shams")

# ---------------


# def increment(number, by):
#     return number + by


# result = increment(2, 1)
# print(result)
"""OR"""
# print(increment(2, 1))
# print(increment(2, by=1))

# ---------------


# def increment(number, by=1):
#     return number + by


# print(increment(2))

# ---------------

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# -----------------

# def save_user(**user):
#     print(user)


# save_user(id=1, name="john", age=25)

# -----------------

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         print("FizzBuzz")
#     elif input % 3 == 0:
#         print("Fizz")
#     elif input % 5 == 0:
#         print("Buzz")
#     else:
#         print(input)


# fizz_buzz(7)

# -----------------

"""List"""
# letters = ["a", "b", "c"]
# matrix = [[1, 2], [3, 4]]
# zeros = 0 * 20
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")

# -----------------

# numbers = list(range(20))
# print(numbers[::2])  # This is show all even numbers
# print(numbers[::-1])  # This is show all numbers in reverse order

# -----------------

"""For unpack the list there is two ways to do that"""
from array import array
numbers = [1, 2, 3, 4]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# forth = numbers[3]
"""OR"""
# first, second, third, forth = numbers

"""But if we just need 2 of them"""
# numbers = [1, 2, 3, 4]
# first, second, *other = numbers
# print(first) # 1
# print(second) # 2
# print(other) # [3, 4]

"""OR"""
# numbers = [1, 2, 3, 4]
# first, *other, last = numbers
# print(first)  # 1
# print(last)  # 4
# print(other)  # [2, 3]

# ----------------

# letters = ["a", "b", "c"]

# for letter in letters:
#     print(letter)
"""OR show in tuple"""
# for letter in enumerate(letters):
#     print(letter)
"""OR unpack the tuple"""
# for index, letter in enumerate(letters):
#     print(index, letter)

# ----------------

# letters = ["a", "b", "c"]

# Add
# letters.append("d") # ["a", "b", "c", "d"]
# letters.insert(0, "-") # ["-", "a", "b", "c"]

# Remove
# letters.pop() # Deleted last item in the list
# letters.pop(0) # Deleted item by index
# letters.remove("a") # ["b", "c", "d"]
"""If we have a multiple "b" only first of them removed"""

# del letters[0:2]  # ["c"]
# letters.clear() # Deleted All item in list

# ----------------

# """Find index"""
# letters = ["a", "b", "c"]
# letters.index("b") # Show you 1 but if "b" not in the list turn to error for this issue we need to use IF
# letters.count("d") # this function show cout of object in the list

# ----------------

# numbers = [5, 4, 32, 25, 11]
# numbers.sort() #[4, 5, 11, 25, 32]
# numbers.sort(reverse=True) #[32, 25, 11, 5, 4]
# sorted(numbers)

# ----------------

# items = [
#     ("Product1", 500),
#     ("Product2", 200),
#     ("Product3", 10),
#     ("Product4", 1500),
#     ("Product5", 350),
# ]
# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
"""OR shorter and cleaner way"""
# items.sort(key=lambda item: item[1])
# print(items)

# ----------------

# items = [
#     ("Product1", 500),
#     ("Product2", 200),
#     ("Product3", 10),
#     ("Product4", 1500),
#     ("Product5", 350),
# ]

# prices = []
# for item in items:
#     prices.append(item[1])

"""OR shorter and cleaner way"""
# prices = map(lambda item: item[1], items)
# print(list(prices))

# ----------------

# items = [
#     ("Product1", 5),
#     ("Product2", 3),
#     ("Product3", 10),
#     ("Product4", 12),
#     ("Product5", 7),
# ]

# x = filter(lambda item: item[1] >= 10, items)

# print(list(x))

# ----------------

# items = [
#     ("Product3", 10, 1500),
#     ("Product1", 9, 500),
#     ("Product4", 12, 2500),
# ]

# prices = list(map(lambda item: item[1], items))
# """OR"""
# prices = [item[1] for item in items]  # shorter and cleaner way ****
# # ----
# filtered = list(filter(lambda item: item[1] >= 10, items))
# """OR"""
# filtered = [item for item in items if item[1]
#             >= 10]  # shorter and cleaner way ****

"""Example"""
# x = [item[2] for item in items]
# print(x)
# y = [item for item in items if item[1] >= 10 and item[2] > 2000]
# print(y)

# -----------

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2))) # [(1, 10), (2, 20), (3, 30)]

# ---------------
# STACKS => LIFO => Last In - First Out
# QUEUES => FIFO => First in - First Out
# ---------------

# x = 10
# y = 11

# x, y = y, x
# -------or--------
# x, y = (11, 10)

# print("x", x)
# print("y", y)

# ---------------

#from array import array
# for know about type code search on google "python3 typecode"
# numbers = array("i", [1, 2, 3])
# print(numbers)

# ---------------

# numbers = [1, 1, 2, 3, 4, 4, 5]
# # only show the unique numbers and delete duplicate numbers {1, 2, 3, 4, 5}
# first = set(numbers)
# print(first)
# second = {1, 1, 2, 3, 4, 4, 5}  # it's just like first {1, 2, 3, 4, 5}
# print(second)
# third = {1, 2, 6, 7, 7}
# # combine two sets to one without duplicated number {1, 2, 3, 4, 5, 6, 7}
# print(first | third)
# print(first & third)  # show shared number in two sets {1,2}
# print(first - third)  # delete numbers are repeat in set in this example only 1 and 2 repeat in third set {3,4,5}
# print(first ^ third)  # show different number in two sets {3, 4, 5, 6, 7}
# we cannot access them using by index like first[0]

# ---------------

"""we have 2-way to define a dictionary"""
point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# -----------------------------------
# print(point["a"]) # we get KeyError if key not in our dict
"""there is two solution for this problem"""
# 1
# if "a" in point:
#     print(point["a"])
# 2
# print(point.get("a"))
# -----------------------------------
# del point["x"] # for delete
# -----------------------------------
# for key in point:
#     print(key, point[key])
# ----or-----
# for key, value in point.items():
#     print(key, value)

# ---------------

# values = []
# for x in range(5):
#     values.append(x*2)  # [0,2,4,6,8]
# ---or-----
# values = [x * 2 for x in range(5)]  # we get list
# values = {x * 2 for x in range(5)}  # we get set
# values = {x: x * 2 for x in range(5)}  # we get dictionary

# print(values)

# ---------------

# values = [x*2 for x in range(10)]  # we get list
# for x in values:
#     print(x)
# values = (x*2 for x in range(10))  # we get generator object
# print(values)
"""generator object it's very usefull and have a lower size than others"""

# ---------------

# Unpacking Operators
# numbers = [1, 2, 3, 4, 5]
# print(*numbers)
# # ---------------------------------
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 3}
# print(combined)

# ---------------

# sentence = "This is a common interview question or not so lets go on"

# my_dict = {}
# for char in sentence:
#     if char in my_dict:
#         my_dict[char] += 1
#     else:
#         my_dict[char] = 1

# my_dict_sorted = sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True)

# if my_dict_sorted[0] != " ":
#     print(my_dict_sorted[1])
# else:
#     print(my_dict_sorted[0])
hi

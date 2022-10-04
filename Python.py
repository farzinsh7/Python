# to see Problems : CTRL + SHIFT + M
# T see Command Pallete : CTRL + SHIFT + P
# to run in terminal : CTRL + ALT + N
# Built in functions: https://docs.python.org/3/library/functions.html
# Math funvtion: https://docs.python.org/3/library/math.html
# ------------------------------------------
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return'FizzBuzz'
#     if input % 3 == 0:
#         return'Fizz'
#     if input % 5 == 0:
#         return'Buzz'
#     return input
# print(fizz_buzz(15))
# ------------------------------------------
# letters = ["a", "b", "c"]
# letters.append("d") --------> add a new value at end of the list
# letters.insert(0, "-") --------> we can insert a value and define the index of that
# letters.pop() --------> we can delete the last item in the list
# letters.pop(0) --------> we can delete the item by index
# letters.remove("c") --------> we can delete the items by value
# del letters[0:2] --------> we can delete a range of items
# letters.clear() --------> for delete entire list
# print(letters)
# ------------------------------------------
# items = [
#     ("produc1", 15),
#     ("produc2", 5),
#     ("produc3", 7)
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)
# -----OR-------
# items = [
#     ("produc1", 15),
#     ("produc2", 5),
#     ("produc3", 7)
# ]

# items.sort(key=lambda item: item[1])
# print(items)
# ------------------------------------------
# items = [
#     ("produc1", 15),
#     ("produc2", 5),
#     ("produc3", 7)
# ]
# prices = list(map(lambda item: item[1], items))
# # -----OR-list comprehension------
# prices = [item[1] for item in items]
# print(prices)
# ------------------------------------------
# items = [
#     ("produc1", 15),
#     ("produc2", 5),
#     ("produc3", 7)
# ]
# filtered = list(filter(lambda item: item[1] % 5 == 0, items))
# # -----OR-list comprehension------
# filtered = [item for item in items if item[1] % 5 == 0]
# print(filtered)
# ------------------------------------------
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip(list1, list2, "abc")))
# ------------------------------------------
# my_list = [1, 2, 3, 4, 5]
# if we want to remove last item of a list we use pop and we call tha STACK
# my_list.pop()
# my_list.pop()
# print(my_list)
# -----
# but if we want to remove first item in the list we use Collections and we call that QUEUE
# from collections import deque
# queue = deque(my_list)
# queue.popleft()
# queue.popleft()
# print(queue)
# -------------------Session 16-----------------------
# numbers = [1, 2, 3, 4, 4, 4]
# first = set(numbers)
# second = {6, 1, 2, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)
# -------------------Session 19-----------------------
# my_dict = {"x": 1, "y": 2}
# print(my_dict)
# my_dict1 = dict(x=2, y=3)
# print(my_dict1)
# -------------------Session 20-----------------------
# values = [x*2 for x in range(5)]  # We get list
# values = {x*2 for x in range(5)}  # We get set
# values = {x: x*2 for x in range(5)}  # We get dictionary
# -------------------Session 21-----------------------
# from sys import getsizeof
# values = (x*2 for x in range(1000000))
# values1 = [x*2 for x in range(1000000)]
# print("Generator:", getsizeof(values))
# print("List:", getsizeof(values1))
# -------------------Session 22-----------------------
# To unpack lists we use *
# To unpack dictionaries we use **
# -------------------Exerciese-----------------------
# from pprint import pprint
# sentance = "This is a common interview question"
# char_frequency = {}
# for char in sentance:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# char_frequency_sorted = sorted(
#     char_frequency.items(),
#     key=lambda kv: kv[1],
#     reverse=True)
# print(char_frequency_sorted[0])
# -------------------Practice-----------------------
# ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# my_dict = {}
# for char in ipsum:
#     if char in my_dict:
#         my_dict[char] += 1
#     else:
#         my_dict[char] = 1
# my_dict_sorted = sorted(
#     my_dict.items(),
#     key=lambda kv: kv[1],
#     reverse=True
# )
# print(my_dict_sorted[1])
# -------------------Exceptions-----------------------
try:
    file = open("coursera\words.txt")
    file.write("hello")
    age = int(input("Enter your Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You Didn't enter a valid age")
else:
    print("No exceptions were thrown.")
finally:
    file.close()

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

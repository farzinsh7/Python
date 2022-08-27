# fname = input("Enter your file: ")
# oname = open(fname)
# myDict = dict()
# myList = list()
# for line in oname:
#     line = line.rstrip()
#     if line.startswith("From "):
#         line = line.split()
#         day = line[2]
#         myList.append(day)
# for item in myList:
#     myDict[item] = myDict.get(item, 0)+1
# lst = list()
# for key, value in myDict.items():
#     lst.append((key, value))
# lst = sorted(lst, reverse=True)
# for k, v in lst:
#     if k == "Thu":
#         k = "Thursday"
#     elif k == "Sat":
#         k = "Saturday"
#     elif k == "Fri":
#         k = "Friday"
#     print(f"You worked {v} Day's in {k}")
# -------------------------
# Python Regular Expression Quick Guide

# ^        با ابتدای یک خط مطابقت دارد
# $        با انتهای یک خط مطابقت دارد
# .        با هر کارکتری مطابقت دارد
# \s       با فضای خالی مطابقت دارد
# \S       با هر کاراکتر بدون فضای سفید مطابقت دارد
# *        یک کاراکتر را صفر یا چند بار تکرار می کند
# *?       یک کاراکتر را صفر یا چند بار تکرار می کند(غیر حریص)
# +        یک کاراکتر را یک یا چند بار تکرار می کند
# +?       یک کاراکتر را یک یا چند بار تکرار می کند(غیر حریص)
# [aeiou]  با یک کاراکتر در مجموعه فهرست شده مطابقت دارد
# [^XYZ]   با یک نویسه که در مجموعه فهرست شده نیست مطابقت دارد
# [a-z0-9] مجموعه کاراکترها می تواند شامل یک محدوده باشد
# (        نشان می دهد که استخراج رشته از کجا شروع می شود
# )        نشان می دهد که استخراج رشته از کجا تموم می شود

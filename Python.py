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

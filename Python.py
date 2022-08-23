# data = "hello there my name is farzin shams you can send me a message if you want here is my email:me@farzinshams.com now guess my website?"
# find_email = data.find("@")
# print(find_email)
# find_space = data.find(" ", find_email)
# print(find_space)
# website = f"You website is: www.{data[find_email+1: find_space]}"
# print(website)
# for letter in 'banana':
#     print(letter)
# text = "X-DSPAM-Confidence:    0.8475"
# find_0 = text.find("0")
# find_num = text[find_0:]
# fnum = float(find_num)
# print(fnum)
# fname = input("Enter you file name: ")
# try:
#     rfile = open(fname)
# except:
#     print("We cant fine your file", fname)
#     quit()

# count = 0
# for line in rfile:
#     if line.startswith("_ "):
#         count += 1
# print(f"There are {count} _ in your file")

# fname = input("Enter file name: ")
# try:
#     fhandle = open(fname)
#     rfile = fhandle.read()
#     rfile.rstrip()
# except:
#     print("Your file not defined!!!")
#     quit()
# print(rfile.upper())
# ---------Assignment 7.2----------
# inputFile = input("Enter file name:")
# fname = open(inputFile)
# count = 0
# calcLine = 0
# for line in fname:
#     if line.startswith("X-DSPAM-Confidence: "):
#         noline = line.rstrip()
#         # print(noline)
#         count += 1
#         fline = line.find("0")
#         tnum = float(line[fline:].rstrip())
#         calcLine += tnum
# print("Average spam confidence:  ", calcLine/count)
# ---------8.1 - Lists----------
# total = 0
# count = 0
# while True:
#     num = input("Enter number: ")
#     if num == "done":
#         break
#     value = float(num)
#     total = total + value
#     count += 1
# average = total / count
# print("Average is: ", average)
# ----or---
# numlist = list()
# while True:
#     num = input("Enter number: ")
#     if num == "done":
#         break
#     value = float(num)
#     numlist.append(value)
# average = sum(numlist)/len(numlist)
# print("Average is: ", average)
# ---------8.3 - Lists and Strings----------
# name = "Farzin sina ali"
# nlist = name.split()
# print(nlist)
# -----
# name = "Farzin;Sina;Ali"
# nlist = name.split(";")
# print(nlist)
# ------
# fname = open("mbox-short.txt")
# for line in fname:
#     line = line.rstrip()
#     if not line.startswith("From "):
#         continue
#     words = line.split()
#     email = words[1].split("@")
#     print(email[1])
# ---------Assignment 8.4---------------
# fname = input("Enter file name: ")
# fh = open(fname)
# myList = list()
# for line in fh:
#     line = line.rstrip().split()
#     for element in line:
#         if element in myList:
#             continue
#         else:
#             myList.append(element)
# myList.sort()
# print(myList)
# ---------Assignment 8.5---------------
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# for line in fh:
#     line = line.rstrip()
#     if line.startswith("From "):
#         line = line.split()
#         print(line[1])
#         count += 1
# print(f"There were {count} lines in the file with From as the first word")
# ------------------Dictionaries-------------------
# myList = [1, 2, 3, 4, 1, 2, 5, 1, 3, 2, 1, 1, 3, 2, 1, 4, 2, 3]
# myDict = dict()
# for num in myList:
#     myDict[num] = myDict.get(num, 0)+1
# print(myDict)
# ------------------Dictionaries-2------------------
# fname = open("romeo.txt")
# myDict = dict()
# for line in fname:
#     line = line.rstrip().split()
#     for elements in line:
#         myDict[elements] = myDict.get(elements, 0)+1
# print(myDict)
# print(myDict.items())
# print(myDict.keys())
# print(myDict.values())
# -------
# fname = open("romeo.txt")
# myDict = dict()
# for line in fname:
#     line = line.rstrip().split()
#     for item in line:
#         myDict[item] = myDict.get(item, 0)+1
# for key, value in myDict.items():
#     print(key, value)
# -------------Assignment 9.4---------------
# fname = input("Enter file name: ")
# oname = open(fname)
# myList = list()
# myDict = dict()
# for line in oname:
#     line = line.rstrip()
#     if line.startswith("From "):
#         line = line.split()
#         myList.append(line[1])
# for item in myList:
#     myDict[item] = myDict.get(item, 0)+1

# bigWord = None
# bigNumber = None
# for word, num in myDict.items():
#     if bigWord is None or num > bigNumber:
#         bigWord = word
#         bigNumber = num

# print(bigWord, bigNumber)
# -------------Tuple---------------
# oname = open("mbox-short.txt")
# myList = list()
# myDict = dict()
# for line in oname:
#     line = line.rstrip()
#     if line.startswith("From "):
#         line = line.split()
#         myList.append(line[1])
# for item in myList:
#     myDict[item] = myDict.get(item, 0)+1

# lst = list()
# for key, value in myDict.items():
#     lst.append((value, key))
# lst = sorted(lst, reverse=True)
# for v, k in lst[:3]:
#     print(k, v)
# -------------Tuple---------------
# fname = input("Enter file name: ")
oname = open("mbox-short.txt")

for line in oname:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        time = line[5].split(":")
        print(time)

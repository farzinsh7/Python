# x = 'farzin'
# y = list()
# z = dict()
# print(dir(x))
# print(dir(y))
# print(dir(z))
# # dir() show you all the methods in different objects
# -------------
# class MyBirthday:
#     x = 0

#     def __init__(self):
#         print('Hello my friend')

#     def birthday(self):
#         self.x += 1
#         print(f"You invite {self.x} People")

#     def __del__(self):
#         print(f"So you invited {self.x} guests in your party")


# invitation = MyBirthday()
# for i in range(0, 10):
#     invitation.birthday()
# ------------------
# class MyCars:
#     x = 0
#     model = ""

#     def __init__(self, z):
#         self.model = z
#         print(f"Your car model is {self.model}")

#     def count(self):
#         self.x += 1
#         print(
#             f"The model of you car is {self.model} and you must save {self.x}K to buy")


# an = MyCars("Benz")
# an.count()
# an.count()
# an.count()
# an = MyCars("Tesla")
# an.count()
# an.count()
# ----------------------
# class PartyAnimal:
#     x = 0
#     name = ""

#     def __init__(self, x):
#         self.name = x
#         print(f"Hi {self.name}")

#     def party(self):
#         self.x += 5
#         print(f"{self.name} arrived at 09:{self.x}")


# class Shout(PartyAnimal):
#     total = 0

#     def count_shout(self):
#         self.total += 1
#         self.party()
#         print(f"{self.name} drink {self.total} shout after 10:{self.x}")

#     def __del__(self):
#         print(
#             f"Now {self.name} is drunk we need to take him to hospital after {self.total} Shouts")


# # call = PartyAnimal("farzin")
# # call.party()
# call_again = Shout('Ali')
# call_again.count_shout()
# call_again.count_shout()
# call_again.count_shout()
# call_again.count_shout()
# ------------
import sqlite3

conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
list_1 = []
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

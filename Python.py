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
# -------------------------
# from urllib.request import Request, urlopen
# import urllib.parse
# import urllib.error
# from bs4 import BeautifulSoup

# url = ('http://py4e-data.dr-chuck.net/comments_1613563.html')
# test = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(test, 'html.parser')
# total = 0
# tags = soup('span')
# for tag in tags:
#     num = int(tag.get_text())
#     total = total + num
# print(total)
# --------------------------
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# link = input('Enter url: ')
# cont = int(input("Enter count: "))
# line = int(input("Enter position: "))

# print(f"Retrieving: {link}")
# for i in range(0, cont):
#     html = urllib.request.urlopen(link, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')

#     tags = soup('a')
#     cn = 0
#     ps = 0
#     for tag in tags:
#         ps += 1
#         if ps == line:
#             print(f"Retrieving: {str(tag.get('href',None))}")
#             link = str(tag.get('href', None))
#             ps = 0
#             break
# -----------------/
# req = Request(
#     url='https://city.hamyar.co/fifteen/',
#     headers={'User-Agent': 'Mozilla/5.0'}
# )
# webpage = urlopen(req).read()
# soup = BeautifulSoup(webpage, 'html.parser')

# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
# --------XML----------
# import xml.etree.ElementTree as ET

# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>007</id>
#             <name>Farzin</name>
#         </user>
#         <user x="20">
#             <id>001</id>
#             <name>Farshad</name>
#         </user>
#     </users>
# </stuff>
# '''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print(f"You have {len(lst)} Users in your list")
# print('*****')
# for item in lst:
#     print('Name:', item.find('name').text)
#     print('ID:', item.find('id').text)
#     print('Security code:', item.get('x'))
#     print('**********')
# ---------Assignment-13---------
# import xml.etree.ElementTree as ET
# from urllib.request import Request, urlopen
# import urllib.parse
# import urllib.error
# url = input('Enter url: ')
# rfile = urlopen(url).read()
# inp = ET.fromstring(rfile)
# lst = inp.findall('comments/comment')
# total = 0
# for num in lst:
#     num = int(num.find('count').text)
#     total += num
# print(total)
# ---------Assignment-14---------
# from urllib.request import Request, urlopen
# import urllib.parse
# import urllib.error
# import json

# url = 'https://py4e-data.dr-chuck.net/comments_1613566.json'
# rurl = urlopen(url).read().decode()
# info = json.loads(rurl)['comments']
# # print(info)
# total = 0
# count = 0
# for item in info:
#     count += 1
#     total = int(item['count'])+total
# print(total)

# -----------------
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    pid = js['results'][0]['place_id']
    print('Place id ', pid)

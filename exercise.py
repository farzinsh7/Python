items = [
    ("produc1", 15),
    ("produc2", 5),
    ("produc2", 2),
    ("produc2", 10),
    ("produc3", 3),
    ("produc3", 7)
]

prices = list(filter((lambda item: item[1] % 5 == 0), items))
print(prices)

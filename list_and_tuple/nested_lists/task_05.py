import sys
fruits = sys.argv[1:]
products = [
    ["молоко", "кефир"],  # молочка
    ["котлеты", "курица", "говядина"]  # мясо
]

products.append(fruits)
print(products)
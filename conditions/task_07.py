import sys

product = sys.argv[1]

products = ["Молоко", "Масло", "Хлеб", "Овсянка", "Яйца"]

if product not in products:
    products.append(product)

products.sort()
products = ", ".join(products)
print(products)


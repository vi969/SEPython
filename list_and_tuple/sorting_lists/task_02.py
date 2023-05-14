import sys
fruits = sys.argv[1:]

products = ["апельсины", "Хлеб"]

products.extend(fruits)
products.sort(key=str.upper)
print(products)
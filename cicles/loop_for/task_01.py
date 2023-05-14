import sys
cash = int(sys.argv[1])

products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]
products_list = []
amount = 0
for product in products:
    amount += product["price"]
    if amount <= cash:
        products_list.append(product["name"])
    else:
        break

products_list = ", ".join(products_list)
print(products_list)
# -----------------------------------------------------

# Получаем
amount = int(sys.argv[1])

# Список с результатом.
my_products = []

# Перебираем товары
for product in products:
    amount = amount - product["price"]
    if amount >= 0:
        my_products.append(product["name"])
    else:
        break

# Вывод результата.
print(", ".join(my_products))
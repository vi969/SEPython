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

basket = []
for product in products:
    if cash - product["price"] >= 0:
        cash -= product["price"]
        basket.append(product["name"])
print(', '.join(basket))
#-----------------------------------------------
# Получаем
amount = int(sys.argv[1])

# Список с результатом.
my_products = []

# Перебираем товары
for product in products:
    if amount <= 0:
        break
    if amount >= product["price"]:
        amount = amount - product["price"]
        my_products.append(product["name"])

# Вывод результата.
print(", ".join(my_products))
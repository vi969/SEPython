import sys
new_products = sys.argv[1]
new_products = new_products.split(", ")
products = ["ананас", "макароны", "помидоры", "яблоки"]
products = products + new_products
products.sort()
print(products)

# -------------------------------------------------------------
import sys

products = ["ананас", "макароны", "помидоры", "яблоки"]

# Получаем новые товары.
new_products = sys.argv[1]

# Создаем список.
new_products = new_products.split(", ")

# Расширяем список.
products.extend(new_products)

# Сортируем список.
products.sort()

# Выводим результат.
print(products)
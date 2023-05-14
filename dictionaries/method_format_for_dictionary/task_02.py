import sys

# Получаем данные.
name = sys.argv[1]
category = sys.argv[2]
price = sys.argv[3]

# Формируем словарь.
product = {
   "name": name,
   "category": category,
   "price": price
}

product_template = "{p[name]} ({p[category]}), {p[price]} руб."

# Форматируем строку данными из словаря.
print(product_template.format(p=product))
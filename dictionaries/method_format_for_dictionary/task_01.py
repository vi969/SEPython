import sys

# Получаем данные.
first_name = sys.argv[1]
last_name = sys.argv[2]
age = sys.argv[3]

# Формируем словарь.
user = {
   "first_name": first_name,
   "last_name": last_name,
   "age": age
}

# Форматируем строку данными из словаря.
print("{u[last_name]} {u[first_name]}, {u[age]}".format(u=user))
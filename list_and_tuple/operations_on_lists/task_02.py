import sys
arg_list = sys.argv[1:]
print(arg_list)
cities = ["Прага", "Вена", "Санкт-Петербург"]
cities  = cities + arg_list
print(cities)

import sys

# Берем срез начиная с 1 индекса.
new_cities = sys.argv[1:]

# Добавляем список.
cities = ["Прага", "Вена", "Санкт-Петербург"] + new_cities

print(cities)
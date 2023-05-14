import sys

# Получаем список автомобилей.
cars = sys.argv[1:]

# Сортируем в обратном порядке.
sorted_cars = sorted(cars, reverse=True, key=str.upper)

# Выводим результат
print(cars)
print(sorted_cars)
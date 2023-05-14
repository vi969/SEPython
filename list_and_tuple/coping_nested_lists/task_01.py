cities = [
    ["Москва", 12000000],
    ["Санкт-Петербург", 5300000],
    ["Новосибирск", 1600000],
    ["Калининград", 480000],
    ["Владивосток", 605000],
    ["Киев", 2900000],
    ["Минск", 2000000]
]

# Создаем копию списка
cities_copy = cities.copy()

# Выводим данные
print(cities)
print(cities_copy)
print(cities == cities_copy)
print(cities is cities_copy)
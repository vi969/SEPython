import sys

year = int(sys.argv[1])

population = [
    144_963_650,  # 2003
    144_168_205,
    143_474_219,
    142_753_551,
    142_220_968,
    142_008_838,
    141_903_979,
    142_856_536,
    142_865_433,
    143_056_383,
    143_347_059,
    143_666_931,
    146_267_288,
    146_544_710,
    146_804_372,
    146_880_432,
    146_780_720,
    146_748_590  # 2020
]

years = []

for pop_year in population:
    if pop_year >= population[year - 2003]:
        years.append(population.index(pop_year) + 2003)

years.sort()
print(", ".join(map(str, years)))
#-------------------------------------------------------
# Получаем годы
year = int(sys.argv[1])

# Вычисляем индекс года.
year_index = year - 2003

# Получаем значение.
year_population = population[year_index]

# Создаем список для хранения результатов.
result = []

# Заводим переменную, в которой будем хранить текущий год.
current_year = 2003

# Перебираем значения в цикле.
for p in population:
    # Если население очередного года больше или равно переданному,
    # то добавляем результат в список result.
    if p >= year_population:
        result.append(str(current_year))

    # Увеличиваем год.
    current_year += 1

# Выводим данные
print(", ".join(result))
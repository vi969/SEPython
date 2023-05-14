import sys
start_year = int(sys.argv[1]) - 2003
end_year = int(sys.argv[2]) - 2003

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

print(population[start_year:end_year + 1])

# -----------------------------------------------

# Получаем годы.
year1 = int(sys.argv[1])
year2 = int(sys.argv[2])

# Приводим к индексам списка.
index1 = year1 - 2003

# Приводим к индексам списка.
index2 = year2 - 2003

# Выводим результат.
# Не забываем в конце добавить 1 для конечного индекса.
print(population[index1:index2 + 1])
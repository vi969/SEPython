import sys
revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}

years = [int(sys.argv[1]), int(sys.argv[2])]
years.sort()
early_year, later_year = years
early_year = revenue.get(early_year, 0)
later_year = revenue.get(later_year, 0)
print(later_year - early_year)
# --------------------------------------------------------

import sys

year1 = int(sys.argv[1])
year2 = int(sys.argv[2])

# Вычисляем максимальный и минимальный год.
max_year = max(year1, year2)
min_year = min(year1, year2)

revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}

# Получаем данные.
rev1 = revenue.get(max_year, 0)
rev2 = revenue.get(min_year, 0)

# Выводим результат.
print(rev1 - rev2)
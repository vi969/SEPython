import sys
year = int(sys.argv[1])
month = int(sys.argv[2])
month_budget = int(sys.argv[3])

start_year = 2019
budget = [
    [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
    [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
    [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
]
budget[year - start_year][month - 1] = month_budget
year_budget = sum(budget[year - start_year]) * 1000

print('{:,}'.format(year_budget).replace(',', ' '))
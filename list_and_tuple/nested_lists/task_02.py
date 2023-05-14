import sys
year = int(sys.argv[1])
month = int(sys.argv[2])
budget = [
    [176, 148, 245, 378, 451, 568, 135, 146, 761, 414, 135, 171],  # 2019
    [211, 175, 301, 474, 569, 721, 158, 172, 972, 521, 158, 205],  # 2020
    [257, 210, 374, 599, 722, 920, 188, 206, 1246, 660, 188, 249]  # 2021
]
month_budget = budget[year - 2019][month - 1]
print(month_budget)
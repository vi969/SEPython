import sys
first_month_index = int(sys.argv[1]) - 1
second_month_index = int(sys.argv[2]) - 1

fin = [
    {"income": 987, "expenses": 345},
    {"income": 1987, "expenses": 1247},
    {"income": 3011, "expenses": 2098},
    {"income": 3400, "expenses": 2798},
    {"income": 1987, "expenses": 1783},
    {"income": 2684, "expenses": 2004},
    {"income": 2008, "expenses": 1555},
    {"income": 2498, "expenses": 2210},
    {"income": 1714, "expenses": 1789},
    {"income": 6971, "expenses": 6971},
    {"income": 345, "expenses": 147},
    {"income": 2487, "expenses": 2101}
]
first_month_profit = fin[first_month_index]["income"] - fin[first_month_index]["expenses"]
second_month_profit = fin[second_month_index]["income"] - fin[second_month_index]["expenses"]

print(second_month_profit - first_month_profit)
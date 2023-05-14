import sys

quarter_num = int(sys.argv[1])

quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}
key_quarter = ["quarter_1", "quarter_2", "quarter_3", "quarter_4"]
key = key_quarter[quarter_num - 1]

quarter_profit = sum(quarters[key])
print(quarter_profit)

import sys

# Получаем номер квартала.
q = sys.argv[1]

# Формируем ключ.
key = "quarter_{}".format(q)

quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}

# Получаем список.
data = quarters[key]

# Высчитываем сумму.
q_sum = sum(data)

# Выводим значение.
print(q_sum)
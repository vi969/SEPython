import sys

data = sys.argv[1].split(":")
num_quarter, income = data
num_quarter = "q{}".format(num_quarter)

revenue2023 = {
   "q1": 50,
   "q2": 200,
   "q3": 400,
   "q4": 300
}
revenue2023[num_quarter] = int(income)
sum_year = sum(revenue2023.values())

fraction_quarter = revenue2023[num_quarter] * 100 / sum_year
print("{:.1f}%".format(fraction_quarter))
# -----------------------------------------------------------------
#  Получаем данные
data = sys.argv[1]

# Разбиваем данные
q_num, q_revenue = data.split(":")

revenue2023 = {
   "q1": 50,
   "q2": 200,
   "q3": 400,
   "q4": 300
}

# Обновляем данные
revenue2023["q" + q_num] = int(q_revenue)

# Вычисляем общую сумму доходов
year_revenue = sum(revenue2023.values())

# Вычисляем процент
q_percent = revenue2023["q" + q_num] * 100 / year_revenue

# Выводим данные
print("{:.1f}%".format(q_percent))

import sys

# Получаем данные из аргументов командной строки.
income = int(sys.argv[1])
tax = int(sys.argv[2])

# Напишите ваш код тут.

profit = income - (income / 100 * tax)
print(round(profit, 2))

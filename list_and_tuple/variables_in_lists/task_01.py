import sys
int()
q1 = int(sys.argv[1])
q2 = int(sys.argv[2])
q3 = int(sys.argv[3])
q4 = int(sys.argv[4])

# Помещаем значения в список.
year = [q1, q2, q3, q4]

# Вычисляем среднее.
avg = sum(year) / len(year)

# Выводим результат.
print("Средний доход: {} руб.".format(int(avg)))

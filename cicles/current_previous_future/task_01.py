import sys
months = sys.argv[1:]

increase = []
previous = 0
for month in months:
    increase.append(int(month) - previous)
    previous = int(month)

print(" ".join(map(str, increase)))

#=============================================
import sys

values = sys.argv[1:]

# Список для хранения значений.
diff_values = []

# Предыдущее значение.
prev_value = 0

for value in values:
    # Вычисляем разницу.
    value = int(value)
    diff = value - prev_value

    # Добавляем в список.
    diff_values.append(str(diff))

    # Обновляем прошлое значение.
    prev_value = value

# Выводим результат.
print(" ".join(diff_values))
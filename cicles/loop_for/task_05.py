import sys

months = sys.argv[1:]

months = list(map(int, months))
max_users = max(months)

compairing = []
for month in months:
    compairing.append(str(month - max_users))

print(' '.join(compairing))
#-------------------------------------------------------
values = sys.argv[1:]

# Сперва вычисляем лучший месяц.
max_value = int(values[0])
for value in values[1:]:
    value = int(value)
    if value > max_value:
        max_value = value

result = []

# Теперь сравнение
for value in values:
    # Вычисляем разницу.
    value = int(value)
    diff = value - max_value

    # Добавляем в список.
    result.append(str(diff))

# Выводим результат.
print(" ".join(result))
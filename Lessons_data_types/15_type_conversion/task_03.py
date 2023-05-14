import sys
# Приводим все данные к float.
price = float(sys.argv[1])
full = float(sys.argv[2])
busy = float(sys.argv[3])

# Расставляем скобки.
amount = (full - busy) * price

# Выводим результат.
print(amount)

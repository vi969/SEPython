import sys

# Делаем замену запятой на точку.
rate = sys.argv[1].replace(",", ".")
dollars = sys.argv[2]

# Приводим все данные к числам.
rate = float(rate)
dollars = int(dollars)

# Считаем
full = dollars * rate

# Выводим результат.
print(dollars, " долларов в рублях = ", full, "руб.")
# второй вариант с конкаценацией, но тогда преобразуем в строки:
#print(str(dollars) + " долларов в рублях = " + str(full) + " руб.")


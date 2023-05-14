import sys

pays = sys.argv[1:]
incomings = []
expences = []

for pay in pays:
    if int(pay) > 0:
        incomings.append(int(pay))
    else:
        expences.append(abs(int(pay)))

incomings_total = sum(incomings)
expences_total = sum(expences)

print(f"Доходы: {incomings_total} руб.", f"Расходы: {expences_total} руб.", sep="\n")

#--------------------------------------------------------------------------------------
values = sys.argv[1:]

# Список с результатом.
income = outcome = 0

# Запускаем цикл.
for value in values:
    value = int(value)

    # Распределяем по переменным.
    if value > 0:
        income += value
    else:
        outcome += value

# Вывод результата. Не забываем привести расходы к положительному числу.
print("Доходы: {} руб.\nРасходы: {} руб.".format(income, outcome * -1))
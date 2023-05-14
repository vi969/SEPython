import sys
events = sys.argv[1:]

colors = []

prev_idx = 0
last_color = 'green'
for idx, event in enumerate(events):
    if int(event) == int(events[prev_idx]):
        colors.append(last_color)
    elif int(event) > int(events[prev_idx]):
        colors.append("green")
        last_color = "green"
    else:
        colors.append("red")
        last_color = "red"
    prev_idx = idx

print(" ".join(colors))
#---------------------------------------------------
import sys

# Получаем все элементы
values = sys.argv[1:]

colors = []

# Считаем, что предыдущий элемент минус бесконечность.
# Это значит, что любой другой элемент будет больше,
# а значит первый гарантировано получит зеленый цвет.
prev_value = float("-inf")

# Перебираем элементы
for value in values:
    value = int(value)

    # Сравниваем текущее значение с предыдущим
    if value > prev_value:
        colors.append("green")
    elif value < prev_value:
        colors.append("red")
    else:
        # Если данные равны, то ставим значение последнего элемента из colors
        colors.append(colors[-1])

    prev_value = value

print(" ".join(colors))


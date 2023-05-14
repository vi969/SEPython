import sys

num_list = sys.argv[1:]
num_min = sorted(num_list, key=int)[0]
num_max = sorted(num_list, key=int)[-1]
print(int(num_min), int(num_max))

# ----------------------------------------------
import sys

# Получаем список чисел, которые изначально записаны строками.
values = sys.argv[1:]

# Сортируем список как числа в порядке возрастания.
values.sort(key=int)

# Выводим минимум и максимум.
print(values[0], values[-1])

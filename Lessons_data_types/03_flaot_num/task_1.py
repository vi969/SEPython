import sys

# Получаем аргументы командной строки и сразу
# преобразовываем их к вещественным числам.
m = float(sys.argv[1])
v = float(sys.argv[2])

e = (m * (v ** 2)) /2
print(e)
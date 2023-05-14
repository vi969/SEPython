import sys

# Получаем целое число из первого аргумента командной строки.
number = int(sys.argv[1])

# Напишите ваш код тут.
x = number // 2
y = number % 2

print(x, y)
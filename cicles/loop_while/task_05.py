import sys
n = int(sys.argv[1])
n_sum = 1
i = 1
while i < n:
   n_sum *= (i + 1)
   i += 1

print(n_sum)
#====================================================

import sys

n = int(sys.argv[1])

# Задаем начальное значение факториала.
factorial = 1

# Начинаем цикл с 2 до n.
i = 2
while i <= n:
    # Вычисляем факториал.
    factorial *= i
    i += 1

print(factorial)
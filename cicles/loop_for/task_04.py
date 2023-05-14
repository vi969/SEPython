import sys

sequence = sys.argv[1:]
#1 2 3 4 5
cumulative_total = 0
cumulative_list = []

for revenue in sequence:
    cumulative_total += int(revenue)
    cumulative_list.append(str(cumulative_total))

print(" ".join(cumulative_list))
# -------------------------------------------
# Альтернативный вариант с использованием функционального программирования

from itertools import accumulate
print(" ".join(map(str, accumulate(map(int, sys.argv[1:])))))
import sys

sequence = sys.argv[1:]
max_num_sequence = []
max_num = float("-inf")
for num in sequence:
    if int(num) > max_num:
        max_num = int(num)
        max_num_sequence.append(num)

print(", ".join(max_num_sequence))
#==========================================
import sys

max_values = []
max_value = float("-inf")  # Изначально считаем, что минимальное значение - это минус бесконечность
for value in sys.argv[1:]:
    value = int(value)
    if value > max_value:
        max_value = value
        max_values.append(str(max_value))

print(", ".join(max_values))
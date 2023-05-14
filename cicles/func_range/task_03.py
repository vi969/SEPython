import sys
digit_01 = int(float(sys.argv[1]) * 10)
digit_02 = int(float(sys.argv[2]) * 10)

float_sequence = []
for num in range(digit_01, digit_02 + 1):
    float_sequence.append(str(num / 10))

print(" ".join(float_sequence))
#-----------------------------------------------
start = float(sys.argv[1])
end = float(sys.argv[2])

# Приводим к целым числам
start = int(start * 10)
# Не забываем добавить 1, чтобы захватить конечное число
end = int(end * 10) + 1

values = []
# Перебираем числа и заполняем список values.
for value in range(start, end):
    values.append(str(value / 10))

print(" ".join(values))
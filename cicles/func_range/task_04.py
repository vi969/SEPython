import sys

digit_01 = float(sys.argv[1])
digit_02 = float(sys.argv[2])
digit_01 = int(float(digit_01) * 10)
digit_02 = int(float(digit_02) * 10)

if digit_02 > digit_01:
    func_range = range(digit_01, digit_02 + 1)
else:
    func_range = range(digit_01, digit_02 - 1, -1)

values = []
for num in func_range:
    values.append(str(num / 10))

print(" ".join(values))
#--------------------------------------------------
start = float(sys.argv[1])
end = float(sys.argv[2])

# Корректировка шага и конечного значения.
if start > end:
    step = -1
    end = int(end * 10) - 1
else:
    step = 1
    end = int(end * 10) + 1

# Формируем начальное значение.
start = int(start * 10)

# Перебираем целые числа с помощью range.
values = []
for value in range(start, end, step):
    values.append(str(value / 10))


print(" ".join(values))
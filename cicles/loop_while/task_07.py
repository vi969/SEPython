numbers = [1, 7, 8, 34, 56, 14, 9]

numbers_sum = 0
i = numbers.__len__()
while i > 0:
    numbers_sum += numbers[i - 1]
    i -= 1

print(numbers_sum)

#-------------------------------------
numbers = [1, 7, 8, 34, 56, 14, 9]

i = s = 0
while i < len(numbers):
    s += numbers[i]
    i += 1

print(s)

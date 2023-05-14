import sys

num_sequence = sys.argv[1:]
len_sequence = num_sequence.__len__()

sum_list = []
i = 0
while i < len_sequence:
    string = str(num_sequence[i])
    len_string = string.__len__()
    j = 0
    sum_num = 0
    while j < len_string:
        sum_num += int(string[j])
        j += 1
    i += 1
    sum_list.append(sum_num)

max_num = max(sum_list)
index_num = sum_list.index(max_num)
print(num_sequence[index_num])


#---------------------------------------------------------

numbers = sys.argv[1:]

# Переменные для хранения максимального результата.
max_sum = 0
max_number = 0

# Основной цикл, который обходит числа.
number_i = 0
while number_i < len(numbers):

    # Вложенный цикл для обхода цифр числа и подсчета суммы.
    digit_i = 0
    current_sum = 0
    while digit_i < len(numbers[number_i]):
        current_sum += int(numbers[number_i][digit_i])
        digit_i += 1

    # Обновляем максимальное число.
    if current_sum > max_sum:
        max_sum = current_sum
        max_number = numbers[number_i]

    number_i += 1

print(max_number)








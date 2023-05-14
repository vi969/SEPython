import sys

# Получаем слово из первого аргумента командной строки.
word = sys.argv[1]

# Напишите ваш код тут.
first_symbol = word[0]
last_symbol = word[-1]
print(first_symbol, last_symbol)
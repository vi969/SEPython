import sys

enimals = sys.argv[1]
enimals = enimals.split()
enimals = sorted(enimals, key=len, reverse=True)

print(enimals[0])

# -----------------------------------------------
import sys

text = sys.argv[1]

# Разбиваем в список.
words = text.split()

# Сортирвем список по длине слова.
words.sort(key=len)

# Выводим самое последнее слово.
print(words[-1])
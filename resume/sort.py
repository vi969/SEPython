import sys
word = sys.argv[1]
word_list = list(word)
word_list.sort(key=str.lower)
word = "".join(word_list)
print(word)

#--------------------------------------
import sys

word = sys.argv[1]

# Преобразовываем строку в список символов.
word = list(word)

# Сортируем список с ключом в нижнем регистре,
# чтобы буквы были в алфавитном порядке, а не в порядке,
# в котором они находятся в кодовой таблице.
word.sort(key=str.lower)

# Склеиваем все элементы списка обратно в строку.
print("".join(word))
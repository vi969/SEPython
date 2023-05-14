import sys
phrase = list(sys.argv[1])

punct = [".", "!", "?"]
modify_list = []
for num, char in enumerate(phrase):
    if char in punct and phrase[num - 1] == " " and phrase[num - 2] != " ":
        del phrase[num - 1]

for num , char in enumerate(phrase):
    modify_list.append(char)

print("".join(modify_list))

#-----------------------------------------------------------------------------
text = sys.argv[1]
text = text.strip()

# Новый текст, начанаем с первых двух символов
new_text = text[:2]

# Перебираем все символы начиная со второго.
for i, c in enumerate(text[2:], 2):
    # Если это знак препинания, то смотрим на два предыдущих знака.
    if c in ".?!":
        if text[i-1] == " " and text[i-2] != " ":
            # Удаляем пробел.
            new_text = new_text[:-1]
    new_text += c

print(new_text)






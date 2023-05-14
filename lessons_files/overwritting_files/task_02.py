import sys

name = sys.argv[1]
template_file = open("template.txt", "r", encoding="utf-8")
insert = template_file.read()
print(insert)
insert = insert.replace('{{  }}', name)
print(insert)
template_file.close()

template_file = open("template.txt", "w", encoding="utf-8")
template_file.write(insert)

import sys

# Получаем имя.
name = sys.argv[1].strip()

# Открываем файл на чтение.
template_file = open("template.txt", "r")

# Читаем данные.
template = template_file.read()

# Делаем замену.
text = template.replace("{{ name }}", name)

# Закрываем файл.
template_file.close()

# Открываем файл на запись.
template_file = open("template.txt", "w")

# Записываем данные.
template_file.write(text)

# Закрыавем файл
template_file.close()


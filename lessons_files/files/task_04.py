import sys

var = sys.argv[1]

get_template = open("template.txt").read()
modify = get_template.replace("{{ name }}", var)
print(modify)

import sys

# Получаем имя.
name = sys.argv[1].strip()

# Открываем файл на чтение.
template_file = open("template.txt")

# Читаем данные.
template = template_file.read()

# Делаем замену.
text = template.replace("{{ name }}", name)

# Выводим данные.
print(text)


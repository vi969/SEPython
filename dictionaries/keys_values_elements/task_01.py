import sys

eng_color = sys.argv[1]
rus_color = sys.argv[2]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}

colors[eng_color] = rus_color
colors_lst = list(colors.keys())
colors_str = ", ".join(colors_lst)
print(colors_str)
#
import sys

# Получаем данные
color_key = sys.argv[1]
color_value = sys.argv[2]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}

# Добавляем новый элемент
colors[color_key] = color_value

# Выводим все ключи
print(", ".join(colors.keys()))

#
# Альтернативный вариант
#

# Добавляем новый элемент
# Используем update и распаковку словаря
colors.update(**{color_key: color_value})
import sys

text = sys.argv[1]

# Очищаем строку, применяем title и добавляем точку.
text = text.strip().title() + "."

# Выводим текст.
print(text)
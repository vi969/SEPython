file_html = open("index.html", encoding="utf-8").read()

start_index_header = file_html.find("<h1>")
end_index_header = file_html.find("</h1>")
header = file_html[start_index_header + 4:end_index_header].strip().upper()

formatted_header = file_html[:start_index_header + 4] + header + file_html[end_index_header:]
print(formatted_header)

# Открываем файл на чтение.
html_file = open("index.html", encoding="utf-8")

# Читаем данные.
html = html_file.read()

# Ищем h1 теги
h1_start = html.find("<h1>")
h1_end = html.find("</h1>")

# Получаем текст заголовка.
header = html[h1_start + 4: h1_end]

# Чистим и приводим к верхнему регистру.
header = header.strip().upper()

# Формируем итоговую стркоу.
text = html[:h1_start + 4] + header + html[h1_end:]

# Выводим данные.
print(text)

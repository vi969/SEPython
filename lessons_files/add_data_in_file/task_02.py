products_file = open("products.txt", "a", encoding="utf-8")
products_file.write("\nМасло\nМясо")

# Открываем файл на дозапись.
products_file = open("products.txt", "a")

# Записываем данные.
products_file.write("\nМасло\nМясо")

# Закрываем файл.
products_file.close()

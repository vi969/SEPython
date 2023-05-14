
list_file_1 = open("shopping_list_1.txt", encoding="utf-8")
list_1 = list_file_1.read()
list_file_1.close()

list_file_2 = open("shopping_list_2.txt", encoding="utf-8")
list_2 = list_file_2.read()
list_file_2.close()

list_file_3 = open("shopping_list_3.txt", encoding="utf-8")
list_3 = list_file_3.read()
list_file_3.close()

total_string = list_1 + "\n" + list_2 + "\n" + list_3

products = total_string.split("\n")
products = sorted(products)

unigue_products = []
for product in products:
    if product not in unigue_products:
        unigue_products.append(product)

unigue_products_str = "\n".join(unigue_products)

open("shopping_list.txt", "w+", encoding="utf_8").write(unigue_products_str)
# ----------------------------------------------------------------------------
# Создаем пустой список, в котором будем хранить все продукты.
products = []

# Открываем все файлы на чтение
file1 = open("shopping_list_1.txt", "r")
file2 = open("shopping_list_2.txt", "r")
file3 = open("shopping_list_3.txt", "r")

# Читаем все данные из файлов в список с помощью readlines(),
# а после расширяем products с помощью extend().
products.extend(file1.readlines())
products.extend(file2.readlines())
products.extend(file3.readlines())

# Испольузем set и list для удаления дублей.
products = list(set(products))

# Сортируем список продуктов.
products.sort()

# Формируем итоговую строку.
products = "".join(products)

# Открываем файл shopping_list.txt на запись и записываем в него результат.
products_file = open("shopping_list.txt", "w+")
products_file.write(products)
products_file.close()

# Альтернативный вариант заполнения списка products:
products = []

# Используем цикл for
for i in [1, 2, 3]:
    file = open("shopping_list_{}.txt".format(i), "r")

    # Вместо extend используем +=
    products += file.readlines()
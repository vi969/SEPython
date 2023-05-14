new_products_file = open("new_products.txt", encoding="koi8-r")
new_products = new_products_file.read()

products_file = open("products.txt", "a", encoding="cp1251")
products_file.write(new_products)

# Открываем файл на дозапись.
products_file = open("products.txt", "a", encoding="cp1251")

# Открыаем файл на чтение
new_products_file = open("new_products.txt", "r", encoding="koi8-r")

# Получаем новые товары.
new_products = new_products_file.read()


# Записываем новые товары в файл.
products_file.write(new_products)
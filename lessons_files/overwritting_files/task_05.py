# open("products.txt", "w", encoding="cp1251").write("иванов, \nпетров, \nсидоров")
products_file = open("products.txt", encoding="cp1251")
products = products_file.read()
products_file.close()

products_file = open("products.txt", "w", encoding="utf-8")
products_file.write(products)
products_file.close()

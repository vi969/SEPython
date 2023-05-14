import sys

# Получаем все цены из аргументов командной строки.
# Каждая цена - это целое число.
bread_price = int(sys.argv[1])
milk_price = int(sys.argv[2])
eggs_price = int(sys.argv[3])

# Считаем среднее и выводим результат.
print((bread_price + milk_price + eggs_price) // 3)
# или
print(int((bread_price + milk_price + eggs_price) / 3))
import sys

name_good = sys.argv[1]
quantity = float(sys.argv[2])
price = float(sys.argv[3])
amount = quantity * price
string_format = "| %-30s | %-6d | %-10.2f | %12.2f |" % (name_good, quantity, price, amount)

print(string_format)

# Получаем данные
name = sys.argv[1]
quantity = int(sys.argv[2])
price = float(sys.argv[3])

# Вычисляем сумму и сразу преобразовываем её к строку.
amount = "%.2f" % (quantity * price)

# Преобразовываем цену
price = "%.2f" % price

# Выводим данные.
print("| %-30s | %-6s | %-10s | %12s |" % (name, quantity, price, amount))


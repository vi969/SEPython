# file_sales = open("sales.txt", "w+", encoding="utf-8")
# file_sales.write("""Иванов С. И.	1000
# Петров И. Л.	3000
# Иванов С. И.	3000
# Сидоров Н. В.	3500
# """)
# file_sales.close()

# max_sale = {}
#
# for line in open("sales.txt", "r", encoding="utf-8"):
#     sale = line.strip("\n").split("\t")
#     name, amount = sale
#     amount = int(amount)
#     if not max_sale:
#         max_sale[name] = amount
#         continue
#     if name in max_sale:
#         max_sale[name] += amount
#     else:
#         max_sale[name] = amount
#
# best_manager = max(max_sale, key=max_sale.get)
#
# print("{}, {}".format(best_manager, max_sale[best_manager]))

#-----------------------------------------------------------------------------------

sales_file = open("sales.txt", encoding="utf-8")

# Словарь для хранения сгруппированных данных по всем менеджерам.
managers = {}

#Переменные для хранения текущего лучшего менеджера и его результата.
best_manager = None
best_result = 0

for sale in sales_file:
    # Получаем данные.
    manager, amount = sale.strip().split("\t")

    # Заполняем словарь.
    if manager not in managers:
        managers[manager] = 0
    managers[manager] += int(amount)

    # Проверяем лучшего менеджера.
    if best_result < managers[manager]:
        best_manager = manager
        best_result = managers[manager]

print(f"{best_manager}, {best_result}")



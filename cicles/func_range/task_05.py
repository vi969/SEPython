import sys

pages = sys.argv[1]
pages_list = pages.split(",")
range_list = []

for page in pages_list:
    if "-" in page:
        page = page.split("-")
        start, end = page
        for num in range(int(start), int(end) + 1):
            if num not in range_list:
                range_list.append(num)
    else:
        if int(page) not in range_list:
            range_list.append(int(page))

range_list.sort()
range_list = ",".join(map(str,range_list))
print(range_list)
#----------------------------------------------------------
pages = sys.argv[1]

# Список страниц для печати
pages_list = []

for element in pages.split(","):
    # Поиск отдельных страниц.
    if element.isdigit():
        if int(element) not in pages_list:
            pages_list.append(int(element))
    # Иначе диапазон.
    else:
        # Получаем начальное и конечное значения.
        start, end = element.split("-")
        # Получаем список страниц
        for page in range(int(start), int(end) + 1):
            if page not in pages_list:
                pages_list.append(page)

# Сортируем список.
pages_list.sort()

# Обратно преобразуем к строке
for i in range(len(pages_list)):
    pages_list[i] = str(pages_list[i])

# Финальный вывод.
print(",".join(pages_list))


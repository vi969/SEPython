# open("q1.txt", "w", encoding="utf-8").write("347")
# open("q2.txt", "w", encoding="utf-8").write("562")
# open("q3.txt", "w", encoding="utf-8").write("907")
# open("q4.txt", "w", encoding="utf-8").write("123")

q1_file = open("q1.txt", encoding="utf-8")
q2_file = open("q2.txt", encoding="utf-8")
q3_file = open("q3.txt", encoding="utf-8")
q4_file = open("q4.txt", encoding="utf-8")

profit_1 = int(q1_file.read())
profit_2 = int(q2_file.read())
profit_3 = int(q3_file.read())
profit_4 = int(q4_file.read())   

year_profit = profit_1 + profit_2 + profit_3 + profit_4

open("year.txt", "w", encoding="utf-8").write(str(year_profit))

# Читаем данные из qN файлов.
q1_file = open("q1.txt")
q1 = q1_file.read().strip()

q2_file = open("q2.txt")
q2 = q2_file.read().strip()

q3_file = open("q3.txt")
q3 = q3_file.read().strip()

q4_file = open("q4.txt")
q4 = q4_file.read().strip()

# Преобразовываем к числу и складывам.
year = int(q1) + int(q2) + int(q3) + int(q4)

# Обратно преобразовываем к строке.
year = str(year)

# Сохраняем в годовой отчет.
year_file = open("year.txt", "w")
year_file.write(year)
year_file.close()
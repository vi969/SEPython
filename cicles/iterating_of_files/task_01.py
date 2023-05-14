file_txt = open("transactions.txt", "w+", encoding="utf-8")
file_txt.write("""Продажа муки;4900
Закуп муки;-1200
Продажа кефира;2900
Продажа молока;-1500
""")

file_txt.close()

result = 0

for note in open("transactions.txt", "r", encoding="utf-8"):
    product, price = note.split(";")
    result += int(price)

print(result)

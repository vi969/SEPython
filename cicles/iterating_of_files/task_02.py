txt_file = open("transactions.txt", "w+", encoding="utf-8")
txt_file.write('''Продажа муки;income;4900
Закуп муки;outcome;1200
Продажа кефира;income;2900
Продажа молока;income;1500
''')
txt_file.close()

balance = 0

for note in open("transactions.txt", "r", encoding="utf-8"):
    note.strip("\n")
    action, transaction, value = note.split(";")
    if transaction == "income":
        balance += int(value.strip())
    else:
        balance -= int(value.strip())

print(balance)
#--------------------------------------------------------------
transactions_file = open("transactions.txt", "r")

total = 0

# Проходимся по всем строкам файла
for transaction in transactions_file:
    # Разбиваем строку на три составляющие
    subject, operation, amount = transaction.split(";")
    # В зависимости от направления платежа увеличиваем или уменьшаем баланс.
    if operation == "income":
        total += int(amount.strip())
    else:
        total -= int(amount.strip())

print(total)
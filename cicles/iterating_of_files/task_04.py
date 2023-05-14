import sys

file_bank = open("bank.txt", "w+", encoding="utf-8")
file_bank.write('''123;456;100
456;789;200
789;123;500
''')
file_bank.close()

account = sys.argv[1]
account_balance = 0
for transaction in open("bank.txt", "r", encoding="utf-8"):
    if account in transaction:
        account_outcome, account_income, amount = transaction.strip().split(";")
        if account == account_outcome:
            account_balance -= int(amount)
        else:
            account_balance += int(amount)

print(account_balance)
#--------------------------------------------------------------------------------------
account = sys.argv[1]
transactions_file = open("bank.txt", "r")

total = 0
for transaction in transactions_file:
    # Получаем все данные по отдельности.
    account_from, account_to, amount = transaction.split(";")

    # Если перевод со счета, то уменьшаем баланс.
    if account_from == account:
        total -= int(amount)

    # Если перевод на счет, то увеличиваем баланс.
    if account_to == account:
        total += int(amount)

print(total)


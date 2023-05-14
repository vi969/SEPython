
import sys

# Получаем данные.
t_from = sys.argv[1]
t_to = sys.argv[2]
amount = sys.argv[3]

# Формируем словарь.
transaction = {
   "from": t_from,
   "to": t_to,
   "amount": amount
}

# Сформируйте правильный шаблон
t_template = "Перевод {t[amount]} руб. со счета {t[from]} на счет {t[to]}."

# Форматируем строку данными из словаря.
print(t_template.format(t=transaction))
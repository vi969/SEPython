from datetime import datetime

# Создаем переменную now типа date.
# Переменная now хранит текущую дату.
now = datetime.now()

# Вывод текущей даты.
# По умолчанию она будет выведена в формате ГГГГ-ММ-ДД.
print("{:%d.%m.%Y}".format(now))

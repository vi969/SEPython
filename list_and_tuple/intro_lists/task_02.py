import sys
first_name = sys.argv[1]
last_name = sys.argv[2]

first_names = ['Иван', 'Пётр', 'Дмитрий', 'Василий']
last_names = ['Антонов', 'Шмидт', 'Лебедев', 'Васильев', 'Шиков']

first_name = first_names[int(first_name) - 1]
last_name = last_names[int(last_name) - 1]
name = "{} {}".format(first_name, last_name).upper()
print(name)


# Получаем данные.
fn_index = int(sys.argv[1]) - 1
ln_index = int(sys.argv[2]) - 1

first_names = ['Иван', 'Пётр', 'Дмитрий', 'Василий']
last_names = ['Антонов', 'Шмидт', 'Лебедев', 'Васильев', 'Шиков']

# Формируем строку.
fl = "{} {}".format(first_names[fn_index], last_names[ln_index])

# Выводим с увеличенным регистром.
print(fl.upper())
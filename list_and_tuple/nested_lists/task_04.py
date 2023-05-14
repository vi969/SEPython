import sys
last_name = int(sys.argv[1])
first_name = int(sys.argv[2])
patronymic = int(sys.argv[3])
fio = [
    ["Иванов", "Юдашкин", "Петров", "Королева", "Коваленко"],  # Фамилии
    ["Юрий", "Андрей", "Никита", "Вероника", "Игнат", "Пётр", "Валерий"],  # Имена
    ["Александрович", "Анатольевна", "Викторовна", "Иванович"]   # Отчества
]
last_name = fio[0][last_name]
first_name = fio[1][first_name]
patronymic = fio[2][patronymic]
fio_str = "{} {} {}".format(last_name,first_name, patronymic)
print(fio_str)
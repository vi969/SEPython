import sys
full_name = sys.argv[1]
full_name = full_name.title()
last_name, first_name, patronymic = full_name.split()
fio_str = "{} {}. {}.".format(last_name, first_name[0], patronymic[0:1])
print(fio_str)

# ------------------------------------------------------------------------------
import sys

# Получаем ФИО.
fio = sys.argv[1]

# Рабиваем по пробелу.
f, i, o = fio.split()

# Выводим данные.
print("{} {}. {}.".format(f.capitalize(), i[0].upper(), o[0].upper()))

#
# Альтернативный вариант.
#
import sys

# Получаем ФИО, приводим к нужному виду и сразу разбиваем.
fio = sys.argv[1].title().split()


# Выводим данные.
print("{fio[0]} {fio[1][0]}. {fio[2][0]}.".format(fio=fio))


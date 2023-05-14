import sys
index_remove = int(sys.argv[1])
marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
del marks[index_remove]
print(marks)

# ----------------------------------------------------------

import sys

# Не забываем преобразовать к int.
index = int(sys.argv[1])

marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]

# Для удаления по индексу, используется метод pop.
marks.pop(index)

print(marks)
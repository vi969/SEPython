import sys
length = len(sys.argv)
print(length - 1)

# --------------------------------

import sys

# Берем срез кроме нулевого элемента.
values = sys.argv[1:]

# Возвращаем длину.
print(len(values))
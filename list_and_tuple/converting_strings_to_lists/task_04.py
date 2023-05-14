import sys
logs = sys.argv[1]
logs = logs.split()
method, adress = logs[2:4]
print(method, adress)

# -----------------------------------
import sys

log = sys.argv[1]

# Разбиваем в список.
parts = log.split(" ")

# Выводим результат.
print("{} {}".format(parts[2], parts[3]))
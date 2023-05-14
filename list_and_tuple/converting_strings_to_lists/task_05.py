# import sys
# logs = sys.argv[1]
# logs = logs.split()
# http_request = logs[4]
# version = http_request.split("/")[1]
# print(version)
# -----------------------------------------
import sys

log = sys.argv[1]

# Разбиваем в список.
parts = log.split(" ")

# Разбираем протокол
protocol = parts[4].split("/")

# Выводим результат.
print(protocol[1])


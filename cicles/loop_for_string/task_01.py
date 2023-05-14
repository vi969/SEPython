import sys

message = sys.argv[1]

code = ""
for char in message:
    if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        code += char

print(code)
#----------------------------------------------------------------------

text = sys.argv[1]

code = ""
# Перебираем текст
for char in text:
    # Если это число, то добавляем к коду.
    if char.isdigit():
        code += char

print(code)
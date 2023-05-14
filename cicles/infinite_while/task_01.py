result = 0
while True:
    number = input("Введите число: ")
    if number == "stop":
        break
    else:
        number = int(number)
        result += number

print(result)


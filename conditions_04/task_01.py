import sys
age = int(sys.argv[1])
hours = int(sys.argv[2])

if age >= 18 and 7 <= hours < 22:
    print("Разрешено")
else:
    print("Запрещено")








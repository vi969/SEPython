import sys
# length = len(sys.argv[1])
length = sys.argv[1].__len__()
if length < 6:
    print("Пароль слишком короткий")
elif length > 8:
    print("Пароль подходит")
else:
    print("Хорошо, но можно и лучше")


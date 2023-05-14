import sys
user_password = sys.argv[1]

if len(user_password) < 6:
    print("Пароль слишком короткий")
else:
    print("Пароль подходит")
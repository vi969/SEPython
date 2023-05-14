import sys
email = sys.argv[1].lower()
password = sys.argv[2]

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"},
    {"email": "user7@domain.com", "password": "123456"},
    {"email": "user8@domain.com", "password": "123456"},
    {"email": "user9@mail.com.ru", "password": "password9"}
]

access_status = "Пользователь не найден"

for user in users:
    if user["email"] == email:
        if user["password"] == password:
            access_status = "Доступ открыт"
        else:
            access_status = "Доступ закрыт"
        break

print(access_status)
#-------------------------------------------------------

# Получаем данные пользователя.
email = sys.argv[1].lower()
password = sys.argv[2]

# Задаем доступ: None - пользователь не найден, True - доступ есть, False - доступа нет.
has_access = None

# Перебираем всех пользователей в цикле:
for user in users:
    if user["email"] == email:
        if user["password"] == password:
            has_access = True
        else:
            has_access = False

        break

# Выводим результат.
if has_access is None:
    print("Пользователь не найден")
elif has_access:
    print("Доступ открыт")
else:
    print("Доступ закрыт")

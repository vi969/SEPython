import sys

user_name = sys.argv[1]
user_password = sys.argv[2]

users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}

if user_name not in users:
    print("Пользователь не найден")
elif users.get(user_name) == user_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")

#-----------------------------------------
# Получаем имя пользователя.
username = sys.argv[1]
password = sys.argv[2]

# Получаем пароль пользователя.
user_password = users.get(username)

if user_password is None:
    print("Пользователь не найден")
elif user_password == password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")

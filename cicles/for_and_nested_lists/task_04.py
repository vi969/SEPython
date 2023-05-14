import sys
language = sys.argv[1]

users = [
    {"id": 17,  "active": False, "langs": ["python", "javascript"]},
    {"id": 156, "active": True,  "langs": ["php"]},
    {"id": 23,  "active": True,  "langs": ["java", "c++"]},
    {"id": 84,  "active": True,  "langs": ["python", "c++"]},
    {"id": 28,  "active": False, "langs": ["java", "php"]},
    {"id": 21,  "active": True,  "langs": ["java", "javascript"]},
    {"id": 55,  "active": True,  "langs": ["python", "c#"]},
    {"id": 88,  "active": True,  "langs": []},
    {"id": 287, "active": False, "langs": ["c++", "c#", "java"]},
    {"id": 481, "active": False, "langs": ["php", "javascript", "python"]},
    {"id": 134, "active": True,  "langs": ["c++", "python"]},
    {"id": 65,  "active": True,  "langs": ["php", "python"]},
     {"id": 7,  "active": False,  "langs": ["javascript", "c#"]}
]

devs = []

for user in users:
    for lang in user["langs"]:
        if lang == language:
            if user["active"] is not True:
                devs.append(user["id"])
print(", ".join(map(str, devs)))
#================================================================================
users_ids = []

for user in users:
    # Проверяем языки и активность.
    if lang in user["langs"] and not user["active"]:
        # Собираем id
        users_ids.append(str(user["id"]))

# Выводим результат.
print(", ".join(users_ids))
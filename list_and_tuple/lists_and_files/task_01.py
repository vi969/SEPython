with open("users.txt", "w+", encoding="utf-8") as  users_file:
    users_file.write("Иванов Дмитрий, 42\nВасильва Светлана, 18\nВарламов Семен, 22\nШмидт Татьяна, 31\n" 
                     "Анисимов Виталий, 22\nАнтонов Денис, 27")
users_file.close()

users_file = open("users.txt", encoding="utf-8")
users = users_file.read().split("\n")
print(users)

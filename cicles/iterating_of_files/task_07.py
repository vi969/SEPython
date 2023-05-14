dict_file = open("dict.txt", "w+", encoding="cp1251")
dict_file.write("""авокадо
воспарить
Спартак
проспорить
спарринг
""")
dict_file.close()

spar_list = []
for word in open("dict.txt", encoding="cp1251"):
    modify_word = word.lower().strip("\n")
    if modify_word.find("спар") >= 0:
        modify_word = modify_word.replace("спар", "SPAR")
        spar_list.append(modify_word)

print("\n".join(spar_list))
#=============================================================
result = []

for line in open("dict.txt", encoding="cp1251"):
    line = line.strip().lower()
    if "спар" in line:
        result.append(line.replace("спар", "SPAR"))

print("\n".join(result))
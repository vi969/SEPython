open("language.txt", "w+", encoding="cp1251").write("English")

lang_file = open("language.txt").read()
print(lang_file)

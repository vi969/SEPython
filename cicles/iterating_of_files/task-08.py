# file_1 = open("data-1.txt", "w+", encoding="utf-8")
# file_1.write("Пгмрае")
# file_2 = open("data-2.txt", "w+", encoding="utf-8")
# file_2.write("ррмон")
# file_3 = open("data-3.txt", "w+", encoding="utf-8")
# file_3.write("оаиви")


import sys

files = int(sys.argv[1])
symbols = int(sys.argv[2])

text = ""
i = 0
while symbols > 0:
    for file_num in range(files):
        if symbols > 0:
            file_name = f"data-{file_num + 1}.txt"
            content = open(file_name, "r", encoding="utf-8").read()
            text += content[i]
            symbols -= 1
        else:
            break
    i += 1
print(text)

#===========================================================================
files_count = int(sys.argv[1])
chars_count = int(sys.argv[2])

# Сперва читаем все данные из файлов в список.
files_data = []
for f in range(1, files_count + 1):
    files_data.append(open(f"data-{f}.txt", "r").read())

char = 0
data = ""
i = 0
# Цикл, пока не закончатся все символы
while char < chars_count:
    # Цикла по данным в файлах.
    for file in files_data:
        if char == chars_count:
            break
        data += file[i]
        char += 1
    i += 1

print(data)
import sys

# Принимаем данные и сохраняем их в переменных disk, catalog1, catalog2, filename
disk, catalog1, catalog2, filename = sys.argv[1], sys.argv[2], sys.argv[3],  sys.argv[4]

print(disk + ":" + "\\" + catalog1 + "\\" + catalog2 + "\\" + filename)
import sys
#
# movie_file = open("films.txt", "w+", encoding="cp1251")
# movie_file.write("""1,Зеленая миля,The Green Mile
# 2,Побег из Шоушенка,The Shawshank Redemption
# 3,Список Шиндлера,Schindler's List
# 4,1+1,Intouchables
# 5,Форрест Гамп,Forrest Gump
# 6,Интерстеллар,Interstellar
# """)
movie_file.close()

name_movie = sys.argv[1].lower()
movie_list = []
for movie in open("films.txt", "r", encoding="cp1251"):
    if movie.lower().find(name_movie) != -1:
        movie_list.append(movie.split(",")[1])

print("\n".join(movie_list))
#----------------------------------------------------------
# name = sys.argv[1].lower()
#
# founded = []
# # Открываем файл в кодировке cp1251
# for line in open("films.txt", "r", encoding="cp1251"):
#     # Получаем элементы строки
#     _, ru_name, en_name = line.strip().split(",")
#
#     # Ищем совпадения
#     if name in ru_name.lower() or name in en_name.lower():
#         founded.append(ru_name)
#
# print("\n".join(founded))
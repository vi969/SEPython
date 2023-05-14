import sys

votes = sys.argv[1:]
# Преобразуем каждый элемент в целое число.
# Элемент функционального программирования, будем изучать в отдельном курсе.
votes = list(map(int, votes))
avg_votes = sorted(votes.copy())
avg_votes = avg_votes[1:-1]
avg_votes = sum(avg_votes) / len(avg_votes)
print("{} {:.2f}".format(votes, avg_votes))
-----------------------------------------------------

import sys
#
# votes = sys.argv[1:]
#
# # Преобразуем каждый элемент в целое число.
# # Элемент функционального программирования, будем изучать в отдельном курсе.
# votes = list(map(int, votes))
#
# # Делаем копию.
# work_votes = votes.copy()
#
# # Сортируем.
# work_votes.sort()
#
# # Убираем крайние значения.
# work_votes = work_votes[1:-1]
#
# # Считаем среднее.
# avg = sum(work_votes) / len(work_votes)
#
# # Выводим список оценок и результат.
# print(votes, "{:.2f}".format(avg))

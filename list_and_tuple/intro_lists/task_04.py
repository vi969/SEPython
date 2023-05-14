import sys

index_01 = int(sys.argv[1])
index_02 = int(sys.argv[2])

languages = ['Python', 'C++', 'JavaScript', 'Java']
val_1 = languages[index_01]
val_2 = languages[index_02]
languages[index_02]  = val_1
languages[index_01]  = val_2

print(languages)

import sys

index1 = int(sys.argv[1])
index2 = int(sys.argv[2])

languages = ['Python', 'C++', 'JavaScript', 'Java']

# Простой алгоритм
temp = languages[index1]
languages[index1] = languages[index2]
languages[index2] = temp

# Альтернативный вариант: обмен в одно действие
languages[index1], languages[index2] = languages[index2], languages[index1]

print(languages)
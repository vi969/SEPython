import sys

index = int(sys.argv[1])
new_lang = sys.argv[2]

languages = ['Python', 'C++', 'JavaScript', 'Java']

languages[index] = new_lang
print(languages)

import sys

# Получаем элементы.
index = int(sys.argv[1])
value = sys.argv[2]

languages = ['Python', 'C++', 'JavaScript', 'Java']

# Делаем замену.
languages[index] = value

print(languages)
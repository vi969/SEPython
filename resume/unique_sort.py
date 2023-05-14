import sys

word = list(sys.argv[1])
word.sort()

sorted_word = []
for letter in word:
    if letter not in sorted_word:
        sorted_word.append(letter)

print("".join(sorted_word))


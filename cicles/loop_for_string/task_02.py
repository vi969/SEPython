import sys

letters = sys.argv[1]

low_letters = upper_letters = ""

for letter in letters:
    if letter.islower():
        low_letters += letter
    else:
        upper_letters += letter

letters = low_letters + upper_letters

print(letters)

import sys

file_name = sys.argv[1]

dot_index = file_name.rfind(".") + 1
file_extension = file_name[dot_index:]
print(file_extension.lower())

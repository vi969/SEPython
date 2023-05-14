import sys

phone_num = sys.argv[1]
phone_num = phone_num.replace("-", " (", 1).replace("-", ") ", 1)
print(phone_num)

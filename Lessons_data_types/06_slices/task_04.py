import sys

phone_num = sys.argv[1]
print(phone_num[:6] + "?" * 5 + phone_num[-2:])
print(len(phone_num))
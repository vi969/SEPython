import  sys
phone_num = sys.argv[1]

is_phone = phone_num.startswith("+7")
print(not is_phone)
import sys
phone_num_format = sys.argv[1]
print("+7 (" + phone_num_format[1:4] + ") " + phone_num_format[-7:-4] + "-" + phone_num_format[-4:-2] + "-" + phone_num_format[-2:] )

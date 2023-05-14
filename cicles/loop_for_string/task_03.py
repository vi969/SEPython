import sys

num_sequence = sys.argv[1:]

negotive_num = positive_num = ""

for num in num_sequence:
    if int(num) < 0:
        negotive_num += num + " "
    else:
        positive_num += num + " "

print(negotive_num + positive_num)

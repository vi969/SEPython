import sys

string = sys.argv[1]
lst = string.split()

sum_digit = 0
i = 0
while i < lst.__len__():
    if int(lst[i]) == 0:
        break
    else:
        sum_digit += int(lst[i])
    i += 1
print(sum_digit)


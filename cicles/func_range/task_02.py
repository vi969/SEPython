import sys
in_num = int(sys.argv[1]) + 1
fac = 1
for num in range(1, in_num):
    fac *= num
print(fac)

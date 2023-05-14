import sys
num = int(sys.argv[1])
string = ""

i = 1
while i <= 9:
    temp = str(num * i)
    string += temp + " "
    i += 1

print(string)

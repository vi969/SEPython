import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]

print(num1.rjust(15, "."), num2.rjust(15, "."),num3.rjust(15, "."), sep="\n")
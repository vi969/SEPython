import sys

sum = sys.argv[1]
sum_end_position = sum.find(".")
print(sum[:sum_end_position])
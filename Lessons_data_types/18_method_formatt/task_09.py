import  sys

digit = sys.argv[1]
digit_class = '{:,d}'.format(int(digit)).replace(",", " ")
print(digit_class)
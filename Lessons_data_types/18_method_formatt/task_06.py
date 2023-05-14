import  sys
digit = float(sys.argv[1])

digit = '{:0=8.2f}'.format(digit)
digit = '{:.>16}'.format(digit)
print(digit)
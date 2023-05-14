import sys

price = sys.argv[1]

if price.endswith('99'):
    print(int(price) + 1)
else:
    print(price)


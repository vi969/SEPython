import sys
num = float(sys.argv[1])

values = [184.414, 174.12, 581, 145.98, 159.1, 824.24]

values = values + [num]
quantity_values = len(values)
sum_values = sum(values)
avg = sum_values / quantity_values
print("{:.3f}".format(avg))
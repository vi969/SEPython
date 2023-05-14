import  sys
index = int(sys.argv[1])

values = [7, 9, 4, 8, 1, 5, 3, 6, 2]
del_index = values.pop(index)
del values[del_index]
print(values)
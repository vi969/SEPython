import sys
num_list = sys.argv[1:]

num_list.sort(key=int, reverse=True)
print(num_list)
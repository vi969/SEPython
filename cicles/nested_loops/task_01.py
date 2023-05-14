# import sys
#
# rooms = int(sys.argv[1])
# floors = int(sys.argv[2])
# string = ""
#
# i = 1
# while i <= floors:
#     j = 1
#     while j <= rooms:
#         string += "{}{} ".format(str(i), str(j))
#         j += 1
#     i += 1
# print(string)

import sys

rooms = int(sys.argv[1])
floors = int(sys.argv[2])

line = []

current_floor = 1
while current_floor <= floors:
    current_room = 1
    while current_room <= rooms:
        line.append("{}{}".format(current_floor, current_room))
        current_room += 1
    current_floor += 1

print(' '.join(line))

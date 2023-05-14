
import sys
final_num = int(sys.argv[1])
quantity_num = int(sys.argv[2])

string = ""
i = 1
while i <= final_num:
    if i % quantity_num != 0:
        string += "{} ".format(i)
    else:
        string += "{}\n".format(i)
    i += 1
print(string)








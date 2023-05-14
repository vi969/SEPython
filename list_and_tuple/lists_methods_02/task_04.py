import sys
mark = int(sys.argv[1])

school_marks = [3, 4, 4, 5, 3, 3, 5, 5, 5, 4, 3, 2, 4, 5, 2, 4, 5]
quantity_of_mark = school_marks.count(mark)
print(quantity_of_mark)
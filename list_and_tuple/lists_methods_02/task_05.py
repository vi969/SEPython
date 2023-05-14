import sys
mark = int(sys.argv[1])

school_marks = [3, 4, 4, 5, 3, 3, 5, 5, 5, 4, 3, 2, 4, 5, 2, 4, 5]

quantity_of_mark = school_marks.count(mark)
total_marks = len(school_marks)
percent = quantity_of_mark * 100 / total_marks
percent_str = "{:.1f}%".format(percent)
print(percent_str)
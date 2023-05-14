import sys
remove_mark = sys.argv[1].strip()
marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
marks.remove(remove_mark)
print(marks)
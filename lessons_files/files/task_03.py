# open("month_salary.txt", "w+", encoding="utf-8").write("10000")
salary_file = open("month_salary.txt").read()
salary_for_year = int(salary_file) * 12
print(salary_for_year)
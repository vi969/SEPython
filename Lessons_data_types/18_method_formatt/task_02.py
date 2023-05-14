import sys

last_name = sys.argv[1]
first_name = sys.argv[2]
birth_year = sys.argv[3]

user_str = "| {:<8} | {:<8} | {:>6} |".format(last_name,first_name,birth_year)

print(user_str)
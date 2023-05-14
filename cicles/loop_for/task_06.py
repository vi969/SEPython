import sys

years = sys.argv[1:]

normalize_years = []

temp = "null"
for year in years:
    if year == "null":
       year = temp
       normalize_years.append(year)
    else:
       temp = year
       normalize_years.append(year)

print(" ".join(normalize_years))



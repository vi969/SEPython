import sys
tax = int(sys.argv[1])
revenue = [178, 351, 145, 764, 514, 456,
           411, 145, 275, 245, 441, 716]

year_revenue = sum(revenue)
sum_tax = (year_revenue / 100) * tax
print(round(sum_tax, 2))
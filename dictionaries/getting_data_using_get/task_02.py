import sys

revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}
first_year = int(sys.argv[1])
second_year = int(sys.argv[2])
first_year_revenue = revenue.get(first_year, 0) or 0
second_year_revenue = revenue.get(second_year, 0) or 0

print(first_year_revenue - second_year_revenue)
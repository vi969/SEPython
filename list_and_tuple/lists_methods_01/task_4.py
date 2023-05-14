import sys
index = int(sys.argv[1])
country = sys.argv[2]
countries = ["Россия", "Украина", "Беларусь"]
countries.insert(index, country)
print(countries)
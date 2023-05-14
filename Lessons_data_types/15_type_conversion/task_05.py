import sys

men_and_women = sys.argv[1]
men = men_and_women.count("m")
women = men_and_women.count("w")
m = "m" + " (" + str(men) + ") " + "*"*men
w = "w" + " (" + str(women) + ") " + "*"*women
print(m)
print(w)

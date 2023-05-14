import sys
quater = sys.argv[1:]
revenue = [178, 351, 0, 764, 514, 0,
           411, 145, 0, 245, 441, 0]
quater = list(map(int, quater))
revenue[2] = quater[0]
revenue[5] = quater[1]
revenue[8] = quater[2]
revenue[11] = quater[3]

first_quater = sum(revenue[:3])
secont_quater = sum(revenue[3:6])
third_quater = sum(revenue[6:9])
fourth_quater = sum(revenue[9:])

print(first_quater, secont_quater, third_quater, fourth_quater)


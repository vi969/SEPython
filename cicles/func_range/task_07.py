import sys
limit = int(sys.argv[1])
total = 1
start = 3
for i in range(1, limit):
    if i % 2 != 0:
        total -= 1 / start
    else:
        total += 1 / start
    start += 2

num_pi = round(total * 4, 5)
print(num_pi)
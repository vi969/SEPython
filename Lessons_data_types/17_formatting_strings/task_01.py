import sys
distance = sys.argv[1]
time = sys.argv[2]

v = float(distance) / float(time)
v_str = "%.2f" %v
print(v_str)
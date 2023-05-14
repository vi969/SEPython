import  sys

t_start = float(sys.argv[1])
t_end = float(sys.argv[2])
wind_speed = float(sys.argv[3])

weather = "%+d°…%+d°, %.1f м/с" %(t_start, t_end, wind_speed)
print(weather)


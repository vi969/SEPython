import sys

color = sys.argv[1]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий",
   "red": "красный",
   "yellow": "желтый"
}
color_item = colors[color]
print(color_item)
print(colors)
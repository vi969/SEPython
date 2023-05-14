import sys

color = sys.argv[1]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}
get_key = colors.pop(color)
colors[get_key] = color
print(colors)

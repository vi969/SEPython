import sys

color_eng = sys.argv[1]
color_rus = sys.argv[2]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}
colors[color_eng] = color_rus
print(", ".join(sorted(list(colors))))
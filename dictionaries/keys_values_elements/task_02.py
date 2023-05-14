import sys

key = sys.argv[1]
value = sys.argv[2]

colors = {
   "black": "черный",
   "white": "белый",
   "blue": "синий"
}
colors[key] = value
colors_lst = list(colors.values())

colors_str = ", ".join(colors_lst)
print(colors_str)
import sys

color = sys.argv[1]
rainbow = {
    "red": "красный",
    "orange": "оранжевый",
    "yellow": "желтый",
    "green": "зеленый",
    "blue": "голубой",
    "indigo": "синий",
    "violet": "фиолетовый"
}
print(rainbow[color])

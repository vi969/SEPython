import sys
dict_key = sys.argv[1]

car = {
    "mark": "Nissan",
    "model": "Qashqai",
    "year": 2018,
    "price": 1_200_000,
    'volume': 2.0
}

print(car.get(dict_key, "неизвестно"))

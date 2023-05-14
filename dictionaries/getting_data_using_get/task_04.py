import sys

sizes = {
    "44": "xs",
    "46": "s",
    "48": "m",
    "50": "l",
    "52": "xl"
}

sex = {
    "m": "m",
    "f": "w",
    "w": "w"
}

model = sys.argv[1].lower().replace(" ", "-")
size = sys.argv[2]
gender = sys.argv[3]

size = sizes.get(size, "all")
gender = sex.get(gender, "unisex")

print(model, size, gender, sep="-")
# -------------------------------------------------------

# Получаем данные
product = sys.argv[1]
size = sys.argv[2]
sex_param = sys.argv[3]


# Выводим результат.
print("{}-{}-{}".format(
    product.lower().replace(" ", "-"),
    sizes.get(size, "all"),
    sex.get(sex_param, "unisex"),
))
import sys

base_price = sys.argv[1]
new_price = sys.argv[2]

product = {
   "name": "Бинокль",
   "price": [base_price, new_price]
}

t_template = "{p[name]}: {p[price][1]} руб."
t_template = t_template.format(p=product)
print(t_template)
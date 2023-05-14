import sys

# Получаем данные.
model = sys.argv[1]
new_price = int(sys.argv[2])
new_count = int(sys.argv[3])

# Исходный словарь.
product = {
    "model": "UE43NU7097U",
    "brand": "Samsung",
    "price": 27990,
    "count": 7
}

# Обновляем данные.
product.update(model=model, price=new_price, count=new_count)

# Выводим результат.
print(product)
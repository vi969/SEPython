# import sys
#
# new_car = sys.argv[1:]
#
# cars = ['BMW', 'Audi', 'Toyota', 'Mazda']
# cars = cars + new_car
# print(cars)
# ---------------------------------------
import sys

new_car = sys.argv[1]

cars = ['BMW', 'Audi', 'Toyota', 'Mazda']

# Помещаем new_car в скобки.
cars += [new_car]

# Выводим cars.
print(cars)

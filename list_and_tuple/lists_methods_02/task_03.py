import sys
mark = sys.argv[1].strip()
model = sys.argv[2].strip()

cars = ["Ford Focus", "Skoda Octavia", "Toyota Prius",
        "Hyundai Solaris", "Volkswagen Polo", "Skoda Rapid"]
car = "{} {}".format(mark, model)
print(car in cars)
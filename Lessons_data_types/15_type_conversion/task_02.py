import sys
mass = sys.argv[1]
height = sys.argv[2]

mass_float = float(mass)
height_float = float(height)

kinetic_energy = int(mass_float * 9.8 * height_float)
print(kinetic_energy)

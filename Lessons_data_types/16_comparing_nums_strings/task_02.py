import sys

age = sys.argv[1]

if int(age) >= 18:
    print("разрешить")
else:
    print("запретить")

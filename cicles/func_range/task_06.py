import sys
end = int(sys.argv[1]) + 1

for num in range(1, end):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
#---------------------------------------
limit = int(sys.argv[1])

for i in range(1, limit + 1):
    result = ""

    # Просто наращиваем строку
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if not result:
        result = i

    print(result)
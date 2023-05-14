import  sys

phone_num = sys.argv[1]
phone_num = phone_num.\
    replace("lee", "8").\
    replace("mu", "5").\
    replace("a", "0").\
    replace(" ", "1").\
    replace("b", "2").\
    replace("e", "3").\
    replace("l", "4").\
    replace("n", "6").\
    replace("o", "7").\
    replace("f", "9")
print(phone_num)


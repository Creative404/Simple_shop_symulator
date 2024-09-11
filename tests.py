def test():
    a = input("a")
    return a


while True:
    b=test()
    print(22)
    if b == "x":
        print(1)
        test()
    elif b=="xx":
        print(2)
        test()
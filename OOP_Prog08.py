def Prog8():
    number = []
    for i in range(10):
        numberinput = int(input(f"Input your number ({i + 1}): "))
        number.append(numberinput)

    print("Even Numbers:")
    for evennumber in number:
        if evennumber % 2 == 0:
            print(evennumber)

Prog8()
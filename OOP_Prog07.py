def Prog7():
    number = []
    for i in range(10):
        numberinput = int(input(f"Input your number ({i + 1}): "))
        number.append(numberinput)

    totalsum = sum(number)

    print("Your numbers: ", number)
    print("Sum of all numbers: ", totalsum)
    
Prog7()
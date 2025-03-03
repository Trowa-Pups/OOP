#Name: Saint Trowa N. Tangco
#Year/Grade/Section: BSCPE 1-2
def Prog1():
    number1 = float(input("Input your first number: "))
    number2 = float(input("Input your second number: "))

    if number1 > number2:
        print("Number 1 is bigger: ", number1)

    elif number1 == number2:
        print("Both numbers are the same")

    else:
        print("Number 2 is bigger: ", number2)

Prog1()
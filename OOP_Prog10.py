#Name: Saint Trowa N. Tangco
#Year/Grade/Section: BSCPE 1-2
def Prog10():
    print("Numbers between 0 to 100 that doesn't end with a zero")
    for number in range(101): #I use range(101) because range(100) is only 0 to 99
        if number % 10 != 0:
            print(number)

Prog10()
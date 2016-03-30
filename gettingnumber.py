def getNumber():
    number = 0
    while number <=10 or number >=50:
        try:
            number = int(input("Enter a number between 10-50: "))
            decimalNumber = number.isdecimal()
            if decimalNumber == True:
                print("Please enter a valid number! ")

        except ValueError:
            print("Please enter a valid number! ")
        number = int(input("Enter a number between 10-50: "))
    print("Done")

getNumber()

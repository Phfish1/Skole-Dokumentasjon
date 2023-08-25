def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def inches_to_cm(inces):
    return inces * 2.54

def game_start():
    number1 = int(input("Enter num1: "))
    number2 = int(input("Enter num2: "))

    print(addition(number1, number2))
    print(subtraction(number1, number2))
    print(multiplication(number1, number2))
    print(division(number1, number2))
    print(inches_to_cm(number1))


game_start()
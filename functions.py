def addition(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))


def substraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1, num2, result))


def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))


def division(num1, num2):
    if num2 == 0.0:
        print("Cant Do Divide by Zero")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))


def power(num1, num2):
    result = num1 ** num2
    print("{0} power of {1} = {2}".format(num1, num2, result))



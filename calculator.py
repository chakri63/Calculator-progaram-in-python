from functions import *
while True:
    print("What is your required operation : ")
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for power operation")
    print("Enter Q to exit")

    choice =input("Enter your choice:")
    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter the Number 1 : "))
    num2 = float(input("Enter the number 2 : "))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        substraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    elif choice == '5':
        power(num1, num2)
    else:
        print("Invalid Choice")
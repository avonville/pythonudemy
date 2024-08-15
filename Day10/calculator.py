import os
import calculator_logo as logo

# Calulator

print(logo.logo)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    if a == 0 or b == 0:
        return 0
    return a * b


def div(a, b):
    if b == 0:
        return "Division by zero"
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    continue_calculation = True

    while continue_calculation:

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(
            f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {calculation_function(num1, num2)}, or type 'n' to start a new calculation: ") == "y":
            num1 = calculation_function(num1, num2)
        else:
            continue_calculation = False
            os.system('cls')
            calculator()


calculator()

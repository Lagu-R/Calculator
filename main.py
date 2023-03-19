# Py Calculator program
from art import logo, dashes, exit
# Add
def add(number1, number2):
    return number1 + number2

# Subtract
def subtract(number1, number2):
    return number1 - number2

# Multiply
def multiply(number1, number2):
    return number1 * number2

# Divide
def divide(number1, number2):
    return number1 / number2

# dictionary of operations where inlcude 4
# add, subtract, multiply and divided 
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
#import logo from art.py module
    print(logo)
# ask user first number 
    num1 = float(input("\nWhat's the first number?: "))
    print(dashes)
    # print all operation keys 
    for symbol in operation:
        print(symbol)
    
    isCalc = True
    while isCalc:
    # ask user to input a operation 
        operation_symbol = input("\nPick an operation: ")
        print(dashes)
    # ask user to input second number.
        num2 = float(input("\nWhat's the next number?: "))
        print(dashes)
    # calculation_function is a variable
    # where placed user's input symbol as 
    # operation  and call funciton  by dictionary value
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
    # print full calculation procedures.
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    # Resume calculation process
        resume = input(f"\nType 'y' to continue calculationg with {answer}, or type 'n' to start a new calculation.: ").lower()
        print(dashes)
        if resume == "y":
            num1 = answer
        elif resume == "n":
            print(dashes)
            print(f"\nFinal answer equal: {answer}.\nStart new calculation.")
            isCalc = False
            calculator()
        else:
            print(dashes)
            print(f"\nFinal answer equal: {answer}.\n")
            print(exit)
            isCalc = False
calculator()
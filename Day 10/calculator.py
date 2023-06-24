import os

logo = ''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

operations = {
 "+" : add,
 "-" : subtract,
 "/" : divide,
 "*" : multiply,
 "**" : exponent
}



def calculator():

    num1 = float(input("What is the first number?: "))

    for sign in operations:
        print(sign)

    terminate = False
    
    while terminate != True:
        action = input("Enter an operator: ")

        num2 = float(input("What is the next number?: "))

        for symbol in operations:
            if action == operations[symbol]:
                answer = operations[symbol](num1, num2)

        print(f"{num1} {action} {num2} = {answer}")

        repeat = input(f"Type 'y' to continue calculating with {answer}. Type 'n' to start a new calculation: ")
        if repeat == "y":
            num1 = answer
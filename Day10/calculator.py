import os
from art import logo

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

    print(logo)

    num1 = float(input("What is the first number?: "))

    for sign in operations:
        print(sign)

    terminate = False
    
    while terminate != True:
        action = input("Enter an operator: ")

        num2 = float(input("What is the next number?: "))

        for symbol in operations:
            if action == symbol:
                answer = operations[symbol](num1, num2)

        print(f"{num1} {action} {num2} = {answer}")

        repeat = input(f"Type 'y' to continue calculating with {answer}. Type 'n' to start a new calculation or 'q' to exit: ")
        if repeat == "y":
            num1 = answer
        elif repeat == "n":
            terminate = True
            os.system('cls')
            calculator()
        else:
            break


calculator()
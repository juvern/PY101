import pdb
import json

LANGUAGE = 'en'

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f"=> {message}")

while True:
    prompt('welcome')
    # Ask the user for the first number.
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt("invalid_number")
        number1 = input()

    # Ask the user for the second number.
    prompt("second_number")
    number2 = input()

    while invalid_number(number2):
        prompt("invalid_number")
        number2 = input()

    # Ask the user for an operation to perform.
    prompt("operation")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("operation_error")
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':
            result = int(number1) + int(number2)
        case '2':
            result = int(number1) - int(number2)
        case '3':
            result = int(number1) * int(number2)
        case '4':
            result = int(number1) // int(number2)

    print(f"The result is {result}")

    prompt("ask_again")
    response = input()

    if response == "N":
        break





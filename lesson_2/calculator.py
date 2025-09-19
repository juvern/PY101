import pdb

def prompt(message):
    print(f"=> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

number1 = 0
number2 = 0
operation = 0

def user_input():
    # Ask the user for the first number.
    prompt()
    number1 = input("Welcome to the Calculator!")

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number")
        number1 = input()

    # Ask the user for the second number.
    prompt('What is the second number?')
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number")
        number2 = input()

    # Ask the user for an operation to perform.
    prompt('''What operation?
            1) Add
            2) Substract
            3) Multiply
            4) Divide''')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3 or 4')
        operation = input()

    return number1, number2, operation

def calculate(number1, number2, operation):
    number1, number2, operation = user_input()
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
    return result

    print(f"The result is {calculate(number1, number2, operation)}")
    prompt('Would like like to perform another operation? Y or N.')    


prompt('Welcome to Calculator!')
print(f"The result is {calculate(number1, number2, operation)}")
response = input()

while response == 'Y':
    print(f"The result is {calculate(number1, number2, operation)}")

# pdb.set_trace()

# Print the result to the terminal.
print(f"The result is {calculate(number1, number2, operation)}")






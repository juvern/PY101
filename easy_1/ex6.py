user_input = int(input("Please enter an integeter greater than 0: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product.')

abbr_operations = {
    's': 'sum',
    'p': 'product',
}

if operation == 's':
    result = 0
    for num in range(1, user_input + 1):
        result = result + num
elif operation =='p':
    result = 1
    for num in range(1, user_input + 1):
        result *= num
else:
    print("Oops. Unknown operation.")

print(f'The {abbr_operations[operation]} of the integers between 1 and {user_input} is {result}')
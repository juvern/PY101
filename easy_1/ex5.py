# def prompt(message):
#     print(f'=>{message}')

# prompt('What is the bill?')
# bill = float(input())

# prompt('What is the tip percentage?')
# tip_percentage = float(input())

# tip = bill * tip_percentage / 100
# total = bill + tip

# print(f'The tip is ${tip:.2f}')
# print(f'The total is ${total:.2f}')

bill = float(input("What is the bill? "))
percentage = float(input("What is the tip percentage? "))

tip = bill * (percentage / 100)
total = bill + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")
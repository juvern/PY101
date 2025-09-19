def prompt(message):
    print(f"=> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

INVALID_MESSAGE = "Hmm... that doesn't look like a valid number. Try again."


print("Let's calculate your mortgage monthly payments in $.")

prompt("What is your total amount?")
total_loan = float(input())

while invalid_number(total_loan):
    prompt(INVALID_MESSAGE)
    total_loan = float(input())

prompt("What is the APR? eg - 0.06")
annual_percentage_rate = float(input())

while invalid_number(annual_percentage_rate):
    prompt(INVALID_MESSAGE)
    annual_percentage_rate = float(input())

prompt("What is the loan duration? in months")
duration_months = float(input())

while invalid_number(duration_months):
    prompt(INVALID_MESSAGE)
    duration_months = float(input())

while invalid_number(duration_months):
    prompt("INVALID_MESSAGE")
    duration_months = float(input())


# Interest compounds monthly
monthly_percentage_rate = annual_percentage_rate / 12

monthly_payment = total_loan * (monthly_percentage_rate / (1 - (1 + monthly_percentage_rate)**(-duration_months)))

print(f"You have provided the following information: loan = {total_loan}, APR = {annual_percentage_rate}, duration = {duration_months} months.  Your monthly payment calculates to ${format(monthly_payment,'.2f')}.")
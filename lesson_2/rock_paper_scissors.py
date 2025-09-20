import random
VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==>{message}")

def display_winner(user, computer):
    if (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'rock' and computer_choice == 'scissors'):
            prompt("You win!")
    elif (user_choice == 'rock' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'rock'):
            prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    # GET user options
    prompt(f'Let\'s play. Choose one: {", ".join(VALID_CHOICES)}')
    user_choice = input()
    while user_choice not in VALID_CHOICES:
        prompt(f'You have not entered a valid choice. Choose one: {", ".join(VALID_CHOICES)}')
        user_choice = input()

    # SET random option
    computer_choice = random.choice(VALID_CHOICES)

    # SHOW the user and computer choice
    prompt(f'You have chosen {user_choice}. The computer has chosen {computer_choice}')

    display_winner(user_choice, computer_choice)

    while True:
        prompt("Do you want to play again? Y or N.")
        play_again = input().lower()
        if play_again.startswith('n') or play_again.startswith('y'):
            break
        else:
            prompt("That's not a valid answer")

    if play_again[0] == 'n':
        break




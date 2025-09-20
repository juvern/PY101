import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
ABBR_VALID_CHOICES = [choice[0:2] if choice[0] == 's' else choice[0:1] for choice in VALID_CHOICES]

ALL_CHOICES = VALID_CHOICES + ABBR_VALID_CHOICES

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

ABBR_TO_VALID = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
}

def prompt(message):
    print(f"==>{message}")

def user_wins(user_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[user_choice]

while True:
    # GET user options
    prompt(f'Let\'s play. Choose one: {", ".join(VALID_CHOICES)}')
    user_choice = input()

    # Accept user choice if there is a partial match - ie r for rock

    while user_choice not in ALL_CHOICES:
        prompt(f'You have not entered a valid choice. Choose one: {", ".join(VALID_CHOICES)}')
        user_choice = input()

    if len(user_choice) <= 2:
        user_choice = ABBR_TO_VALID[user_choice]

    # SET random option
    computer_choice = random.choice(VALID_CHOICES)

    # SHOW the user and computer choice
    prompt(f'You have chosen {user_choice}. The computer has chosen {computer_choice}')

    if user_wins(user_choice, computer_choice):
        prompt("You win!")
    else:
        prompt("Computer wins!")

    while True:
        prompt("Do you want to play again? Y or N.")
        play_again = input().lower()
        if play_again.startswith('n') or play_again.startswith('y'):
            break
        else:
            prompt("That's not a valid answer")

    if play_again[0] == 'n':
        break

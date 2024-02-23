from game_data import data
from art import logo, vs
import random
import time
from replit import clear


def get_random_account():
    """Get a random account number."""
    return random.choice(data)


def format_data(account):
    """Format the account data for display."""
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name} a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Check if the user's answer is correct."""
    if a_followers < b_followers:
        return guess == 'A'
    else:
        return guess == 'B'


def game():
    """Run the main game loop."""
    score = 0
    should_continue = True
    a_account = get_random_account()
    b_account = get_random_account()
    while should_continue:
        # Display the logo and rules
        print(logo)
        a_account = b_account
        b_account = get_random_account()
        while a_account == b_account:
            b_account = get_random_account()
        print("Which of the below account has more follower? \n")
        print("Account A: ", format_data(a_account))
        print(f"{vs}\n")
        print("Account B: ", format_data(b_account))
        guess = input("\nType 'A' or 'B':\n").upper()
        is_correct = check_answer(
            guess, a_account['follower_count'], b_account['follower_count'])
        if is_correct:
            score += 1
            print(f"\nCorrect answer.")
            time.sleep(0.4)
            clear()

        else:
            print(f"\nIncorrect answer!.")
            should_continue = False


game()

"""Number Guesser Game - Main Entry Point.

Author: https://github.com/AmiinMohammadi
"""

import random

from utils.evaluate_guess import evaluate_guess
from utils.show_score import show_score
from utils.validation_input import validate_input


def main():
    """Run the main loop of the Number Guesser game."""
    MIN_RANGE = 0
    MAX_RANGE = 100
    user_score = 10

    print("Hi!\nYou'r welcome")
    rnd_num = random.randint(MIN_RANGE, MAX_RANGE)

    print("I chose a number")
    show_score("Your score", user_score)

    while True:
        input_user = input("\nWhat's your guess (or 'exit'): ").lstrip().lower()

        if input_user == "exit":
            print("Bye!")
            break

        user_guess, error_text = validate_input(input_user, MIN_RANGE, MAX_RANGE)

        if error_text:
            print(error_text)
            continue

        user_score, msg, is_win = evaluate_guess(user_guess, rnd_num, user_score)

        print(msg)
        show_score("Your score", user_score)

        # Check if the player won or lost to handle restarts or exits
        if is_win or user_score == 0:
            ask_new_game = input("You want to play again? (y/n): ").lstrip().lower()
            if ask_new_game == "n":
                print("Bye!")
                break
            user_score = 10
            rnd_num = random.randint(MIN_RANGE, MAX_RANGE)
            print("I chose a number")


if __name__ == "__main__":
    main()

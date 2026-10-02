"""Rock Paper Scissors Game - Main Entry Point.

Author: https://github.com/AmiinMohammadi
"""

import random

from utils.evaluate_actions import evaluate_actions
from utils.print_menu import print_menu
from utils.validation_input import validate_input

# Valid actions of game
game_actions = ["rock", "paper", "scissors"]


while True:
    print_menu(game_actions )
    input_user = (
        input("Type one action: (or 'exit'): ").strip().replace(" ", "").lower()
    )
    if input_user == "exit":
        if input("Are you sure? (y/n): ").strip().replace(" ", "").lower() == "y":
            print("Goodbye!")
            break
        continue

    user_action, error_text = validate_input(input_user, game_actions)

    if error_text:
        print(error_text)
        continue
    computer_choice = random.choice(game_actions)

    print("\n——————————————")
    print("Computer choice:", computer_choice)
    print(evaluate_actions(user_action, computer_choice))
    print("——————————————")

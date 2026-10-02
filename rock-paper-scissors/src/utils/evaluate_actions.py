def evaluate_actions(user_action: str, computer_choice: str) -> str:
    """Evaluation actions of user and computer based on logic game.

    :param user_action: user's input.
    :param computer_choice: random choice of computer.
    :return: a string that specify user is winner or not.
    """
    if user_action == computer_choice:
        return "Draw!"

    winning_rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }
    if winning_rules[user_action] == computer_choice:
        return "You won!"

    return "You lost ):"


if __name__ == "__main__":
    evaluate_actions("scissors", "paper")

def evaluate_actions(user_action: str, computer_choice: str) -> str:
    """Evaluation actions of user and computer base on logic game.

    :param user_action: user's input.
    :param computer_choice: random choice of computer.
    :return: a string that specify user is winner or not.
    """
    if user_action == computer_choice:
        return "equal!"

    if (
        (user_action == "rock" and computer_choice == "scissors")
        or (user_action == "paper" and computer_choice == "rock")
        or (user_action == "scissors" and computer_choice == "paper")
    ):

        return "You won!"

    return "You lost ):"


if __name__ == "__main__":
    evaluate_actions("scissors", "paper")

from typing import List, Tuple


def validate_input(action: str, game_actions: List[str]) -> Tuple[str, str]:
    """A function to validate user's input.

    :param action: that must be one of items of game_actions list in src/main.py
    :param game_actions: acceptable game actions
    :return: validate action,error msg
    """

    if action in game_actions:
        return action, ""

    option = ", ".join(game_actions)
    return "", f"Action must be {option}\nTry Again"


if __name__ == "__main__":
    validate_input("paper", ["rock", "paper", "scissors"])

# utils/validation_input.py
from typing import Tuple


def validate_input(input_user: str, min_range: int, max_range: int) -> Tuple[int, str]:
    """Validate the user's input to ensure it is an integer within the specified range.

    :param input_user: The raw string entered by the user.
    :param min_range: The minimum allowed value (inclusive)..
    :param max_range: The maximum allowed value (inclusive)..

    :return: A tuple containing the validated integer guess (or -1 if invalid)
             and an error message string (empty if valid).
    """
    try:
        guess = int(input_user)
        if min_range <= guess <= max_range:
            return guess, ""
        return -1, f"Guess must be between {min_range} to {max_range}\nTry Again"

    except ValueError:
        return -1, "Guess must be number\nTry Again"


if __name__ == "__main__":
    validate_input("50", 0, 100)

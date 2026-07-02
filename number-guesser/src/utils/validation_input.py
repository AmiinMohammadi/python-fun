def validate_input(input_user, min_range, max_range):

    try:
        guess = int(input_user)
        if min_range <= guess <= max_range:
            return guess, ""
        return -1, f"Guess must be between {min_range} to {max_range}\nTry Again"

    except ValueError:
        return -1, "Guess must be number\nTry Again"


if __name__ == "__main__":
    validate_input(50, 0, 100)

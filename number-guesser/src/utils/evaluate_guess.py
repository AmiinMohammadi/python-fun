from typing import Tuple


def evaluate_guess(guess: int, rnd_num: int, score: int) -> Tuple[int, str, bool]:

    if guess == rnd_num:
        return score, "Correct Answer!\nYou won", True

    if (score := score - 1) == 0:
        return score, "You don't have any chance.\nGame Over!", False

    if guess > rnd_num:
        return score, f"{guess} is too high", False
    else:
        return score, f"{guess} is too low", False

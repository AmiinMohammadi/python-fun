import random
from typing import List


def play(doors: List[str], keep: bool) -> bool:
    """
    Simulates a single round of the Monty Hall game.

    :param doors: A list of strings representing what is behind each door (e.g., ['car', 'goat', 'goat']).
    :param keep: Whether the player decides to stick with their initial choice (True) or switch (False).

    :return: True if the player wins the car, False otherwise.
    """

    # Shuffle the doors to randomize the positions of the car and goats
    random.shuffle(doors)

    # Make an initial random choice from the available doors
    first_choice = random.choice(range(len(doors)))

    if keep:
        # Strategy 1: Player sticks with their initial choice
        final_choice = first_choice
    else:
        # Strategy 2: Player switches. Host opens a door revealing a goat.
        # The revealed door cannot be the player's initial choice and must contain a goat.
        goat_door = next(
            i for i in range(len(doors)) if i != first_choice and doors[i] == "goat"
        )
        # Player switches to the remaining unopened door
        final_choice = next(
            i for i in range(len(doors)) if i != first_choice and i != goat_door
        )

    # Check if the final chosen door contains the car
    return doors[final_choice] == "car"


# Define the initial layout: 1 car and 2 goats
doors = ["car"] + ["goat"] * 2

win = 0
try_count = 100_000

# Run simulation for the "Keep" strategy
for _ in range(try_count):
    if play(doors, keep=True):
        win += 1
print((win / try_count) * 100)

win = 0

# Run simulation for the "Switch" strategy
for _ in range(try_count):
    if play(doors, keep=False):
        win += 1
print(win / try_count * 100)

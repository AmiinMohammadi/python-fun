import random
from pathlib import Path
from typing import List

import pandas as pd
import streamlit as st


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


def main():
    # Define the initial layout: 1 car and 2 goats
    doors = ["car"] + ["goat"] * 2

    image_path = Path(__file__).resolve().parent / "assets" / "banner.png"
    if image_path.exists():
        st.image(image_path)
    st.title("Monty Hall Simulation ")

    try_count = st.number_input(
        "Enter count of game play:", min_value=10, max_value=100_000, value=1_000
    )

    # Initialize counters and data list for tracking cumulative wins
    keep_wins = 0
    switch_wins = 0
    sim_data = []

    if st.button("Start Simulation"):
        # Run simulations and calculate running win percentages
        for i in range(1, try_count + 1):
            if play(doors.copy(), keep=True):
                keep_wins += 1
            if play(doors.copy(), keep=False):
                switch_wins += 1

            # Append current progress data
            sim_data.append({
                "Iteration": i,
                "Stick Strategy": (keep_wins / i) * 100,
                "Switch Strategy": (switch_wins / i) * 100,
            })

        # Convert the simulation history to a Pandas DataFrame
        df = pd.DataFrame(sim_data)
        df.set_index("Iteration", inplace=True)

        # UI Layout: Display columns for final metrics
        column1, column2 = st.columns(2)

        final_keep_rate = (keep_wins / try_count) * 100
        final_switch_rate = (switch_wins / try_count) * 100

        column1.subheader("Win percentage without switching")
        column1.metric(label="Final Stick Win Rate", value=f"{final_keep_rate:.2f}%")

        column2.subheader("Win percentage with switching")
        column2.metric(label="Final Switch Win Rate", value=f"{final_switch_rate:.2f}%")

        # Display the live convergence chart
        st.write("### Win Rate Convergence Chart")

        # If user sets a huge number of trials (e.g., 100k+),
        # rendering every single point will lag the browser. We sample the dataframe if needed.

        if try_count > 20_000:
            step = try_count // 200
            st.line_chart(
                df.iloc[::step],
                x_label="Number of games played",
                y_label="Percentage (%)",
            )
        else:
            st.line_chart(
                df, x_label="Number of games played", y_label="Percentage (%)"
            )
        st.success("Simulation successfully!")


if __name__ == "__main__":
    main()

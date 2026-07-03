# 🎲 Number Guesser Game
A fun, interactive, and modular command-line game where the computer selects a random number, and the player tries to guess it before running out of points.

---
## 📂 Project Structure

```text
├── src/
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       ├── evaluate_guess.py
│       ├── show_score.py
│       └── validation_input.py
└── README.md
```
---
## 🛠️ Tech Stack

- Python 3.8+ (Required for the Walrus Operator `:=`)

---
## 🕹️ How to Play
1. **Launch the game:** Execute the script in your terminal (see instructions below).

2. **Make a Guess:** The computer will pick a secret number between 0 and 100. Type your guess and press 'Enter'.

3. **Analyze the Feedback:**

- If your guess is too high, you'll see '[Your Guess] is too high'.

- If it's too low, you'll see '[Your Guess] is too low'.

4. **Win or Lose:**

- Win: Guess the exact number before your score hits 0.

- Lose: If your score drops to 0, the game ends. You can choose to restart or exit.

5. **Exit Anytime:** Type 'exit' during your turn to quit the game.
---
## 💻 How to Run

1. **Install Python:** Make sure Python is installed on your operating system.

2. **Execute the App:** Run the following command from the root directory of the project:

```shell
python src/main.py
```

# Python Fun 🎮

A collection of small, fun Python projects — simple terminal games and playful scripts built for learning and experimentation.

Each project is self-contained in its own folder with its own detailed `README.md` and `LICENSE`. This file is just a high-level overview.

## Projects

| Project | Description | Link |
|---|---|---|
| happy-numbers | Check whether a number is a Happy Number. | [./happy-numbers](./happy-numbers) |
| monty-hall | Interactive Streamlit simulator for the Monty Hall problem. | [./monty-hall](./monty-hall) |
| number-guesser | Terminal number-guessing game — guess the secret number before your score runs out. | [./number-guesser](./number-guesser) |
| rock-paper-scissors | Classic Rock, Paper, Scissors game in the terminal. | [./rock-paper-scissors](./rock-paper-scissors) |
| tic-tac-toe | Object-oriented Tic-Tac-Toe game in the terminal. | [./tic-tac-toe](./tic-tac-toe) |

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/AmiinMohammadi/python-fun.git
   cd python-fun
   ```

2. Go into any project folder and follow its own `README.md` for full details. Quick start:

   ```bash
   # happy-numbers
   cd happy-numbers
   python main.py

   # number-guesser
   cd ../number-guesser
   python src/main.py

   # rock-paper-scissors
   cd ../rock-paper-scissors
   python src/main.py

   # tic-tac-toe
   cd ../tic-tac-toe
   python src/main.py

   # monty-hall (Streamlit app)
   cd ../monty-hall
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Requirements

* Python 3.8+
* For `monty-hall`: additional packages listed in its `requirements.txt` (Streamlit, pandas).

See each project's `README.md` for exact setup steps.

## License

MIT — each project includes its own `LICENSE` file. See the individual project folders for details.

<img src="assets/banner.png">

---

# Monty Hall Problem Simulator

An interactive web application built with **Streamlit 1.58** to simulate and visualize the famous **Monty Hall problem**. This simulator demonstrates the mathematical convergence of win probabilities between two classic choices: sticking with the initial choice vs. switching to the other unopened door.

## 🚀 Features

* **Interactive Simulation:** Choose anywhere from 10 to 100,000 game iterations.
* **Live Convergence Chart:** Watch how the win rates stabilize around the theoretical probabilities ($33.3\%$ for sticking, $66.6\%$ for switching) over time.
* **Performance Optimization:** downsampling for higher trial runs (over 20,000 iterations) to maintain smooth, lag-free UI rendering.
---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have Python installed on your system. You will need `streamlit` and `pandas` to run the simulation and display the interactive graphical web interface.

### Installation

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/AmiinMohammadi/Monty-Hall-Simulation.git
   
   cd Monty-Hall-Simulation
   ```
2. **Install dependencies**:

    Install all the required packages directly from the `requirements.txt` file using `pip`:

    ```bash
    pip install -r requirements.txt
    ```
---

## 💻 How to Run

Launch the Streamlit server by executing the following command in your 
terminal:
```bash
streamlit run app.py
```
Once running, your browser will automatically open the application at http://localhost:8501.

---

## 🧠 How the Simulation Works

The app implements two distinct strategies over $N$ iterations:

1. **Stick Strategy**: The player locks in their initial random choice.

2. **Switch Strategy**: The host reveals a goat behind one of the remaining doors. 

The player then switches to the last unopened door.According to the Law of Large Numbers, as the number of games played increases, you will observe the **Switch Strategy** consistently securing roughly a **2/3 (~66.67%)** win rate, while the **Stick Strategy** trails at **1/3 (~33.33%)**.

**Note**: This simulation uses strict mathematical isolation for both strategies, ensuring unbiased random shuffling per run via Python's standard `random` library.

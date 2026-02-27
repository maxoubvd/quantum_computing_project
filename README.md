# Quantum Tic-Tac-Toe

A quantum-inspired implementation of the classic Tic-Tac-Toe game using Qiskit for quantum computations and Tkinter for the graphical user interface.

## Features

- **Quantum Gameplay**: Utilizes quantum superposition and entanglement to create a unique gaming experience where moves are in superposition until collapsed.
- **Classical Version**: Includes a traditional Tic-Tac-Toe implementation with AI using the Minimax algorithm.
- **Player vs Player (PvP) Quantum Mode**: A two-player quantum mode where both players make quantum moves and have a limited number of collapses each.
- **Graphical Interface**: User-friendly GUI built with Tkinter for interactive play.
- **AI Opponent**: Simple AI for the quantum version that makes random moves on available squares.
- **Main Menu**: A launcher to easily switch between game modes (Classical, Quantum vs AI, PvP).
- **Superposition & Entanglement**: Players place marks in superposition across two squares; upon collapse, quantum measurement determines the outcome.
- **Limited Collapses**: In quantum modes, players have a limited number of voluntary collapses, adding a strategic layer to the game.

## Project Structure

- `main.py`: Main menu launcher — entry point to select between Classical, Quantum (vs AI), and Versus (PvP) modes.
- `quantum_engine.py`: Contains the `QuantumEngine` and `QuantumManager` classes for handling quantum circuits and game state.
- `quantum_ai.py`: Implements a basic AI opponent for the quantum game.
- `quantum_gui.py`: GUI for the Quantum Tic-Tac-Toe game (Player vs AI).
- `quantum_pvp.py`: GUI for the Quantum Player vs Player mode.
- `classical_engine.py`: Classical Tic-Tac-Toe engine with Minimax AI.
- `main_gui.py`: GUI for the classical Tic-Tac-Toe game.
- `requirements.txt`: List of Python dependencies.
- `TODO.md`: Remaining tasks and known issues.

## Installation

1. Ensure you have Python 3.x installed.
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
   The project depends on: `qiskit`, `qiskit_aer`, and `pylatexenc`.

   > Note: Tkinter is usually included with Python installations.

## Usage

### Main Menu (Recommended)
Launch the main menu to choose a game mode:
```
python main.py
```
From the menu you can select:
- **Classical Game** — standard Tic-Tac-Toe vs Minimax AI
- **Quantum Game** — quantum Tic-Tac-Toe vs a random AI
- **Versus Mode** — quantum Tic-Tac-Toe, Player vs Player

### Classical Tic-Tac-Toe
Can also be launched directly:
```
python main_gui.py
```
- Click on a square to make your move as 'X'.
- The AI will respond as 'O' using the Minimax algorithm.

### Quantum Tic-Tac-Toe (vs AI)
Can also be launched directly:
```
python quantum_gui.py
```
- Click on **two squares** to make a move in superposition.
- Squares in superposition are displayed as `X?`, `O?`, or `XO` (when both players share a square).
- Press **"COLLAPSE"** to measure the quantum state and resolve the board (you have 4 collapses).
- A collapse is also triggered automatically when a square has both `X?` and `O?` (becomes `XO`).
- The game continues until a winner is determined or the board is full.

### Quantum PvP (Player vs Player)
Can also be launched directly:
```
python quantum_pvp.py
```
- Two players take turns placing quantum moves (each selecting two squares per turn).
- Each player has **3 collapses** available.
- The same superposition and collapse mechanics apply as in the AI version.

## How It Works

### Quantum Version
- Moves are made by selecting two squares, creating a superposition state.
- The quantum circuit uses an X gate, a Hadamard gate, and a CNOT gate so that exactly one of the two selected qubits ends up as `|1⟩` after measurement.
- Upon collapse, the measurement determines which square gets the mark.
- This allows for probabilistic outcomes and the possibility of multiple winners.

### Classical Version
- Standard Tic-Tac-Toe rules with a perfect AI opponent.
- Uses the Minimax algorithm for optimal play.

## Dependencies

- **Qiskit**: For quantum circuit creation
- **Qiskit Aer**: Quantum simulator backend
- **pylatexenc**: Required for circuit visualization
- **Tkinter**: For GUI (built-in with Python)

## Quantum Circuit

At the end of a game, a picture of the quantum circuit is generated (`quantum_circuit.png`).

## AI Tools

1. AI is used to generate the structure of the Minimax algorithm and to integrate the Tkinter library, saving time on the interface.

   - Advantages: quick setup
   - Disadvantages: need to verify the winning logic (Done, it is working)

2. AI is also used to learn how to use the Qiskit library and implement it for our project.
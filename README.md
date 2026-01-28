# Quantum Tic-Tac-Toe

A quantum-inspired implementation of the classic Tic-Tac-Toe game using Qiskit for quantum computations and Tkinter for the graphical user interface.

## Features

- **Quantum Gameplay**: Utilizes quantum superposition and entanglement to create a unique gaming experience where moves are in superposition until collapsed.
- **Classical Version**: Includes a traditional Tic-Tac-Toe implementation with AI using the Minimax algorithm.
- **Graphical Interface**: User-friendly GUI built with Tkinter for interactive play.
- **AI Opponent**: Simple AI for the quantum version that makes random moves on available squares.

## Project Structure

- `quantum_engine.py`: Contains the `QuantumEngine` and `QuantumManager` classes for handling quantum circuits and game state.
- `quantum_ai.py`: Implements a basic AI opponent for the quantum game.
- `quantum_gui.py`: GUI for the quantum Tic-Tac-Toe game.
- `classical_engine.py`: Classical Tic-Tac-Toe engine with Minimax AI.
- `main_gui.py`: GUI for the classical Tic-Tac-Toe game.
- `AI_tools.md`: Documentation on AI-assisted development aspects.

## Installation

1. Ensure you have Python 3.x installed.
2. Install required dependencies:
   ```
   pip install qiskit qiskit-aer tkinter
   ```
   Note: Tkinter is usually included with Python installations.

## Usage

### Quantum Tic-Tac-Toe
Run the quantum version:
```
python quantum_gui.py
```
- Click on two squares to make a move in superposition.
- Press "COLLAPSE" to measure the quantum state and update the board.
- The game continues until a winner is determined or the board is full.

### Classical Tic-Tac-Toe
Run the classical version:
```
python main_gui.py
```
- Click on a square to make your move as 'X'.
- The AI will respond as 'O' using the Minimax algorithm.

## How It Works

### Quantum Version
- Moves are made by selecting two squares, creating a superposition state.
- The quantum circuit uses Hadamard gates and CNOT gates to entangle the qubits.
- Upon collapse, the measurement determines which square gets the mark.
- This allows for probabilistic outcomes and multiple possible winners.

### Classical Version
- Standard Tic-Tac-Toe rules with perfect AI opponent.
- Uses Minimax algorithm for optimal play.

## Dependencies

- Qiskit: For quantum circuit simulation
- Qiskit Aer: Quantum simulator backend
- Tkinter: For GUI (built-in with Python)

## Quantum circuit

At the end of a game, an picture of the Quantum circuit is generated (quantum_circuit.png)

## AI Tools

1. AI is used to generate the structure of the Minimax algorithm and to integrate the Tkinter library, saving time on the interface.

- Advantages: quick setup
- Disadvantages: need to verify the winning logic (Done, it is working)

2. AI is also use to learn how to use the Qiskit library and implement it for our project.
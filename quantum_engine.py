from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QuantumEngine:
    def __init__(self):
        self.circuit = QuantumCircuit(9, 9)
        self.simulator = AerSimulator()

    def add_move(self, s1, s2):
        # We prepare the state so that ONLY ONE of the two qubits is at 1 (50/50)
        self.circuit.x(s2) 
        self.circuit.h(s1)
        self.circuit.cx(s1, s2)

    def collapse(self):
        try:
            self.circuit.draw(output='mpl', filename='quantum_circuit.png')
            print("Circuit visual saved as quantum_circuit.png")
        except Exception as e:
            print(f"Could not save circuit image: {e}")
        self.circuit.measure(range(9), range(9))
        job = self.simulator.run(self.circuit, shots=1)
        res = list(job.result().get_counts().keys())[0][::-1]
        self.circuit = QuantumCircuit(9, 9) # Reset for the next steps if needed
        return res

class QuantumManager:
    def __init__(self, engine):
        self.engine = engine
        self.history = []
        self.fixed_marks = [' ' for _ in range(9)]

    def record(self, s1, s2, player):
        self.engine.add_move(s1, s2)
        self.history.append({'sq': (s1, s2), 'p': player})

    def get_board(self):
        bits = self.engine.collapse()
        # We fill the board according to the measurement results
        # Process each move: for entangled qubits, exactly one should be '1'
        for m in self.history:
            s1, s2 = m['sq']
            # Check which qubit measured as '1' and place the mark there
            # Only place a mark if the square is still empty (handle overlapping superpositions)
            if bits[s1] == '1' and self.fixed_marks[s1] == ' ':
                self.fixed_marks[s1] = m['p']
            elif bits[s2] == '1' and self.fixed_marks[s2] == ' ':
                self.fixed_marks[s2] = m['p']
            # If both are '0' (shouldn't happen with proper entanglement), pick s1
            elif bits[s1] == '0' and bits[s2] == '0' and self.fixed_marks[s1] == ' ':
                self.fixed_marks[s1] = m['p']
        self.history = [] 
        return self.fixed_marks
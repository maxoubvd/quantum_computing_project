import tkinter as tk
from tkinter import messagebox
import main_gui
import quantum_gui

class MainMenu():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quantum Tic-Tac-Toe Project")
        self.btns = [tk.Button(self.root, text='Classical Game', font=('Arial', 15), height=5, width=15, command=self.classical_game),
                     tk.Button(self.root, text='Quantum Game', font=('Arial', 15), height=5, width=15, command=self.quantum_game)]
        for i, btn in enumerate(self.btns):
            btn.grid(row=i, column=0, padx=10, pady=10)
        
    def classical_game(self):
        self.root.destroy()
        main_gui.ClassicalGUI().root.mainloop()

    def quantum_game(self):
        self.root.destroy()
        quantum_gui.QuantumGUI().root.mainloop()

if __name__ == "__main__":
    MainMenu().root.mainloop()
import tkinter as tk
from tkinter import messagebox
from classical_engine import TicTacToeEngine, minimax

class ClassicalGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Classical Tic-Tac-Toe")
        self.game = TicTacToeEngine()
        self.btns = [tk.Button(self.root, text=' ', font=('Arial', 20), height=2, width=5, 
                     command=lambda i=i: self.click(i)) for i in range(9)]
        for i, btn in enumerate(self.btns): btn.grid(row=i//3, column=i%3)

    def click(self, i):
        if self.game.make_move(i, 'X'):
            self.refresh()
            if not self.check_end(): self.root.after(500, self.ai_move)

    def ai_move(self):
        move = minimax(self.game, 'O')['position']
        if move is not None:
            self.game.make_move(move, 'O')
            self.refresh()
            self.check_end()

    def refresh(self):
        for i in range(9): self.btns[i].config(text=self.game.board[i])

    def check_end(self):
        if self.game.current_winner or not self.game.available_moves():
            res = f"{self.game.current_winner} wins!" if self.game.current_winner else "Tie!"
            messagebox.showinfo("End", res); self.root.destroy(); return True
        return False

if __name__ == "__main__":
    ClassicalGUI().root.mainloop()
import tkinter as tk
from tkinter import messagebox
from quantum_engine import QuantumEngine, QuantumManager
from quantum_ai import QuantumAI

class QuantumGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ESILV - Quantum Challenger")
        self.mgr = QuantumManager(QuantumEngine())
        self.ai = QuantumAI()
        self.sel = []
        self.player = 'X'
        self.collapse_count = 3
        self.btns = [tk.Button(self.root, text=' ', font=('Arial', 20), height=2, width=5,
                     command=lambda i=i: self.click(i)) for i in range(9)]
        for i, btn in enumerate(self.btns): btn.grid(row=i//3, column=i%3)
        tk.Button(self.root, text="COLLAPSE", bg="orange", command=self.do_collapse).grid(row=3, column=0, columnspan=3, sticky="we")

    def nbr_free_squares(self, player):
        free_squares = [b['text'] for b in self.btns if (b['text'] != player + '?' and b['text'] != 'XO')]
        nbr = len(free_squares)
        return nbr

    def click(self, i):
        if self.nbr_free_squares(self.player) < 2:
            self.do_collapse()
        elif len(self.sel) == 2:
            self.mgr.record(self.sel[0], self.sel[1], self.player)
            self.sel = []
            self.player = 'O'
            self.root.after(500, self.ai_turn)
        else:
            # You cannot click on a square that has already been fixed (definitive X or O)
            if self.btns[i]['text'] in ['X', 'O'] or i in self.sel: return

            # You cannot click on a square that is already in a superposed state
            if self.btns[i]['text'] == 'XO': return

            self.sel.append(i)
            # If square already has O? (AI's superposition), create mixed superposition XO
            if self.btns[i]['text'] == 'O?':
                self.btns[i].config(text='XO', bg='red')
            # Otherwise, show player's superposition state
            else:
                self.btns[i].config(text=f"{self.player}?", bg="cyan")

            if self.nbr_free_squares(self.player) < 2:
                self.root.after(500, self.do_collapse)

            elif len(self.sel) == 2:
                self.mgr.record(self.sel[0], self.sel[1], self.player)
                self.sel = []
                self.player = 'O'
                self.root.after(500, self.ai_turn)

    def ai_turn(self):
        # The AI ​​can play on any unfixed square, even if there is already a "?".
        texts = [b['text'] for b in self.btns]
        move = self.ai.get_move(texts)
        if move:
            self.mgr.record(move[0], move[1], 'O')
            for m in move: 
                if self.btns[m]['text'] not in ['X', 'O']:
                    # If square already has X? (player's superposition), create mixed superposition XO
                    if self.btns[m]['text'] == 'X?':
                        self.btns[m].config(text='XO', bg='red')
                    # Otherwise, show AI's superposition state
                    else:
                        self.btns[m].config(text="O?", bg="pink")
            self.player = 'X'

    def check_winner(self, b):
        lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        winners = set()
        for l in lines:
            if b[l[0]] == b[l[1]] == b[l[2]] and b[l[0]] != ' ':
                winners.add(b[l[0]])
        return list(winners)

    def do_collapse(self):
        board = self.mgr.get_board()
        for i in range(9):
            self.btns[i].config(text=board[i], bg="SystemButtonFace")
        
        winners = self.check_winner(board)
        if winners:
            msg = f"Winner(s): {' and '.join(winners)}" if len(winners) > 1 else f"Winner: {winners[0]}"
            messagebox.showinfo("Game Over", msg)
            self.root.destroy()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.root.destroy()
        else:
            messagebox.showinfo("Quantum Info", "No winner. The board is now classical. Keep playing!")

if __name__ == "__main__":
    QuantumGUI().root.mainloop()
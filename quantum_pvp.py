import tkinter as tk
from tkinter import messagebox
from quantum_engine import QuantumEngine, QuantumManager

class PvP:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ESILV - Quantum Player VS Player")
        self.mgr = QuantumManager(QuantumEngine())
        self.playerX = 'X'
        self.playerO = 'O'
        self.players = [self.playerX, self.playerO]
        self.current_player_id = 0
        self.collapse_count = [3, 3]
        self.colour = ['cyan', 'pink']
        self.sel = []  # Initialize selection list
        self.btns = [tk.Button(self.root, text=' ', font=('Arial', 20), height=2, width=5,
                     command=lambda i=i: self.click(i)) for i in range(9)]
        for i, btn in enumerate(self.btns): btn.grid(row=i//3, column=i%3)
        tk.Button(self.root, text="COLLAPSE", bg="orange", command=lambda: self.do_collapse(on_click=True)).grid(row=3, column=0, columnspan=3, sticky="we")

    def nbr_free_squares(self, player):
        free_squares = [b['text'] for b in self.btns if (b['text'] != player + '?' and b['text'] != 'XO')]
        nbr = len(free_squares)
        return nbr

    def next_player(self):
        self.current_player_id = (self.current_player_id + 1) % 2
    
    def click(self, i):
        self.player = self.players[self.current_player_id]
        if self.nbr_free_squares(self.player) < 2:
            self.do_collapse()
        elif len(self.sel) == 2:
            return  # Already have 2 selections, shouldn't happen
        elif len(self.sel) == 1:
            # Second selection
            if self.btns[i]['text'] in ['X', 'O'] or i in self.sel: return
            if self.btns[i]['text'] == 'XO': return
            
            self.sel.append(i)
            if (self.btns[i]['text'] == 'O?' and self.player == 'X') or (self.btns[i]['text'] == 'X?' and self.player == 'O'):
                self.btns[i].config(text='XO', bg='red')
            else:
                self.btns[i].config(text=f"{self.player}?", bg=self.colour[self.current_player_id])
            
            # Now we have 2 selections, record the move
            self.mgr.record(self.sel[0], self.sel[1], self.player)
            self.sel = []
            if self.check_superposition():
                self.root.after(200, lambda: self.do_collapse(bypass=True))
            self.root.after(500, self.next_player)
        else:
            # First selection
            if self.btns[i]['text'] in ['X', 'O'] or i in self.sel: return
            if self.btns[i]['text'] == 'XO': return

            self.sel.append(i)
            if (self.btns[i]['text'] == 'O?' and self.player == 'X') or (self.btns[i]['text'] == 'X?' and self.player == 'O'):
                self.btns[i].config(text='XO', bg='red')
            else:
                self.btns[i].config(text=f"{self.player}?", bg=self.colour[self.current_player_id])

            if self.nbr_free_squares(self.player) < 2:
                self.root.after(500, lambda: self.do_collapse(bypass=True))
    def check_winner(self, b):
        lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        winners = set()
        for l in lines:
            if b[l[0]] == b[l[1]] == b[l[2]] and b[l[0]] != ' ':
                winners.add(b[l[0]])
        return list(winners)

    def do_collapse(self, on_click=False, bypass=False):
        if (self.collapse_count[self.current_player_id] > 0 and on_click) or bypass:
            board = self.mgr.get_board()
            if on_click:
                self.collapse_count[self.current_player_id] -= 1
                msg = f"Player {self.player} used a collapse! {self.collapse_count[self.current_player_id]} collapses left for this player."
                messagebox.showinfo("Collapse Action", msg)
            for i in range(9):
                self.btns[i].config(text=board[i], bg="SystemButtonFace")
            self.sel = []  # Clear selection after collapse
            self.manage_winner(board)
        else:
            msg = f"Player {self.player} has no collapse left!"
            messagebox.showinfo("Collapse Action", msg)
    
    def manage_winner(self, board):
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

    def check_superposition(self):
        for b in self.btns:
            if b['text'] == "XO":
                return True
        return False

if __name__ == "__main__":
    PvP().root.mainloop()

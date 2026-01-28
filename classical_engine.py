import math

class TicTacToeEngine:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([s == letter for s in row]): return True
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in col]): return True
        if square % 2 == 0:
            d1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in d1]): return True
            d2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in d2]): return True
        return False

def minimax(state, player):
    max_p = 'O'
    other_p = 'X' if player == 'O' else 'O'
    if state.current_winner == other_p:
        return {'position': None, 'score': 1*(len(state.available_moves())+1) if other_p == max_p else -1*(len(state.available_moves())+1)}
    elif not state.available_moves():
        return {'position': None, 'score': 0}

    best = {'position': None, 'score': -math.inf if player == max_p else math.inf}
    for move in state.available_moves():
        state.make_move(move, player)
        score = minimax(state, other_p)
        state.board[move] = ' '; state.current_winner = None
        score['position'] = move
        if (player == max_p and score['score'] > best['score']) or (player != max_p and score['score'] < best['score']):
            best = score
    return best
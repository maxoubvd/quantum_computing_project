import random

class QuantumAI:
    def __init__(self, letter='O'):
        self.letter = letter

    def get_move(self, board_texts):
        # AI can play on any square that isn't a FIXED mark or an already mixed superposed state (XO).
        # AI can play on squares with single player superposition (X? or O?) to create XO
        avail = [i for i, text in enumerate(board_texts) if (text not in ['X', 'O']) and (text != 'XO')]
        if len(avail) < 2: return None
        return random.sample(avail, 2)
import random 
from base import Agent 
from hextypes import Point 
from board import Move

class RandomBot(Agent):
    def select_move(self, game_state):
        candidates = game_state.legal_moves()

        if not candidates:
            return Move.resign()
        
        return random.choice(candidates)
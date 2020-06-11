import random 
from base import Agent 
from hextypes import Point 
from board import Move

class Human(Agent):
    def select_move(self, game_state):
        candidates = game_state.legal_moves()

        if not candidates:
            return Move.resign()
        
        move = ""
        while True:
            move = input("Please enter your move in the format FromColRow:DestColRow. Example (A1:A2): ") 
            print('')
            move = move.upper()  

            if move in [c.name() for c in candidates]:
                break
            elif move == "QUIT":
                return Move.resign()
            else:
                print("Invalid move. Please specify a valid move!")

        return self.get_move_by_name(candidates, move)             

    def get_move_by_name(self, candidates, name):
        for candidate in candidates:
            if candidate.name() == name:
                return candidate         

        return None                 
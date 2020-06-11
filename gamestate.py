import copy 
from board import Board
from hextypes import Player
from board import Move

class GameState():
    def __init__(self, board, next_player, previous, move):
        self.board = board 
        self.next_player = next_player 
        self.previous_state = previous 
        self.last_move = move 

    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.apply_move(move)
        else:
            next_board = self.board 
        
        return GameState(next_board, self.next_player.other, self, move)

    def is_over(self):
        if self.last_move is None:
            return False 
        if self.last_move.is_resign: 
            return True 
        if self.board.pawn_reached_end():
            return True        
        if self.board.get_white_pawn_count() == 0 or self.board.get_black_pawn_count() == 0:
            return True 
        
        return False 

    def legal_moves(self):        
        return self.legal_moves_by_color(self.next_player)
        
    def legal_moves_by_color(self, color):        
        candidates = []

        for pawn in self.board.get_pawns(color):
            for next_pos in pawn.position.next(color.direction):                
                if self.board.is_on_board(next_pos) and not self.board.is_blocked(pawn, next_pos):
                    candidates.append(Move.move_pawn(pawn, pawn.position, next_pos))

        return candidates            

    def get_legal_move_count(self, color):
        return len(self.legal_moves_by_color(color))

    def get_pawn_count(self, color):
        return len(self.board._pawns[color])

    def winner(self):
        if self.is_over():     
            if self.last_move.is_resign or self.last_move is None:
                return self.next_player  
            else:       
                return self.next_player.other
        else:
            return None

    @classmethod 
    def new_game(cls, board_size, white, black):
        if isinstance(board_size, int):
            board_size = (board_size, board_size) 
        board = Board(*board_size, white, black) 
        return GameState(board, Player.white, None, None)


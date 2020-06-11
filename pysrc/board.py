import copy  
from hextypes import Player 
from hextypes import Point 

class Move():
    def __init__(self, pawn=None, old_position=None, new_position=None, is_resign=False):
        assert (pawn is not None) ^ is_resign 
        self.pawn = pawn 
        self.is_play = (self.pawn is not None)
        self.old_position = old_position 
        self.new_position = new_position 
        self.is_resign = is_resign 

    # Gives the move a proper name based on the source:dest move.
    def name(self):
        if self.is_resign:
            return "Resign"
        else:
            return self.old_position.name() + ":" + self.new_position.name()

    @classmethod 
    def move_pawn(cls, pawn, old_position, new_position):
        return Move(pawn=pawn, old_position=old_position, new_position=new_position) 
    
    @classmethod 
    def resign(cls):
        return Move(is_resign=True)

class Pawn():
    def __init__(self, name, color, position):
        assert (position is not None)

        self.name = name 
        self.color = color
        self.position = position 
    
class Board():
    def __init__(self, num_rows=3, num_cols=3, white="", black=""):
        self.num_rows = num_rows 
        self.num_cols = num_cols 
        self.white = white 
        self.black = black 
        self._pawns = {}
        self.__setboard__()

    def apply_move(self, move):
        pawn = self.get_pawn_by_name(move.pawn.name)
        if pawn is not None:
            existing_pawn_color = self.get_at_point(move.new_position)
            if existing_pawn_color is not None:
                self.remove_pawn(existing_pawn_color, move.new_position)
            pawn.position = move.new_position         

    # Remove a pawn from the board if it's been captured.
    def remove_pawn(self, color, position_to_remove):
        pawns = [] 
        for p in self._pawns[color]:
            if not (p.position.row == position_to_remove.row and p.position.col == position_to_remove.col):
                pawns.append(p)
        self._pawns[color] = pawns

    def get_at_point(self, point):
        for v in self._pawns[Player.white]:
            if v.position.row == point.row and v.position.col == point.col:
                return Player.white 

        for v in self._pawns[Player.black]:
            if v.position.row == point.row and v.position.col == point.col:
                return Player.black 
        
        return None

    def get_white_pawn_count(self):
        return len(self._pawns[Player.white])

    def get_black_pawn_count(self):
        return len(self._pawns[Player.black])

    def get_pawns(self, player):
        return self._pawns[player]
    
    def get_pawn_by_name(self, name):
        for v in self._pawns[Player.white]:
            if v.name == name:
                return v

        for v in self._pawns[Player.black]:
            if v.name == name:
                return v
        
        return None        

    def is_on_board(self, point):
        if point.row < 1 or point.row > self.num_rows or \
           point.col < 1 or point.col > self.num_cols: 
            return False 
        else:
            return True

    # Returns True if any pawn reached the opposite end of the board
    def pawn_reached_end(self):            
        for v in self._pawns[Player.white]:
            if v.position.row == self.num_rows:
                return True

        for v in self._pawns[Player.black]:
            if v.position.row == 1:
                return True

        return False 

    def is_blocked(self, pawn, dest_point):
        # If moving up or down along the same column and there's already a pawn, 
        # we're not going to be able to move.
        if pawn.position.col == dest_point.col and \
            self.get_at_point(dest_point) is not None:
            return True 
        
        # If we're moving diagonal, there has to be a pawn of the opposite color, otherwise we can't move there.
        if pawn.position.col != dest_point.col and \
            self.get_at_point(dest_point) != pawn.color.other:
            return True

        return False         

    # For debugging: Sets the board to a pre-configured format for manual testing.
    def __setboard_preconfig__(self):
        white_pawns = []
        black_pawns = []

        white_pawns.append(Pawn(name='White ' + str(1), color=Player.white, position=Point(1, 1)))
        white_pawns.append(Pawn(name='White ' + str(2), color=Player.white, position=Point(1, 2)))
        black_pawns.append(Pawn(name='Black ' + str(2), color=Player.black, position=Point(self.num_rows, 2)))
        black_pawns.append(Pawn(name='Black ' + str(1), color=Player.black, position=Point(self.num_rows, 1)))
            
        self._pawns[Player.white] = white_pawns 
        self._pawns[Player.black] = black_pawns 
        
    # Sets the board up with the pawns
    def __setboard__(self):                
        white_pawns = []
        black_pawns = []

        for col in range(1, self.num_cols + 1):
            white_pawns.append(Pawn(name='White ' + str(col), color=Player.white, position=Point(1, col)))
            black_pawns.append(Pawn(name='Black ' + str(col), color=Player.black, position=Point(self.num_rows, col)))
            
        self._pawns[Player.white] = white_pawns 
        self._pawns[Player.black] = black_pawns 


            

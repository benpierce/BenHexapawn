import enum 
from collections import namedtuple 

class Player(enum.Enum): 
    black = 1
    white = 2 

    @property 
    def other(self):
        return Player.black if self == Player.white else Player.white 

    # Black moves down on the grid, White moves up.
    @property 
    def direction(self):
        return -1 if self == Player.black else 1        

class Point(namedtuple('Point', 'row col')):
    def next(self, direction):
        return [
            Point(self.row + direction, self.col - 1),
            Point(self.row + direction, self.col),
            Point(self.row + direction, self.col + 1)
        ]        

    # Gives the point a friendly name
    def name(self):
        COLS = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
        return COLS[self.col - 1] + str(self.row)        

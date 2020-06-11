import hextypes 
import os 

COLS = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
STONE_TO_CHAR = {
    None: ' . ',
    hextypes.Player.black: ' b ',
    hextypes.Player.white: ' w ',
}

def print_move(player, move):
    if move.is_resign: 
        move_str = 'resigns' 
    else: 
        prev_str = '%s%d' % (COLS[move.old_position.col - 1], move.old_position.row)
        move_str = '%s%d' % (COLS[move.new_position.col -1], move.new_position.row) 
        print('')
        print('Last Move: %s %s -> %s' % (player, prev_str, move_str))

def print_intro(board):
    print('--------------------------------------------------------')
    print("Welcome to Ben Pierce's implementation of Hexapawn!")    
    print("")
    print("White (w) = " + board.white) 
    print("Black (b) = " + board.black)
    print("Type Quit to resign.")        
    print('--------------------------------------------------------')
    print("")

def print_board(board, turn, is_over = False, player = None, move = None):
    #os.system('cls')
    print('--------------------------------------------------------')
    print('Turn: {0}'.format(turn))
    if player is not None and is_over == False:
        print("Player: {0}".format(player.other))  

    if move is not None: 
        print_move(player, move)

    print("Type Quit to resign.")        
    print('--------------------------------------------------------')
    print("")
    for row in range(board.num_rows, 0, -1):  
        bump = " " if row <= 9 else "" 
        line = [] 
        for col in range(1, board.num_cols + 1):
            stone = board.get_at_point(hextypes.Point(row=row, col=col)) 
            line.append(STONE_TO_CHAR[stone]) 
        print('%s%d %s' % (bump, row, ''.join(line)))  

    print('    ' + '  '.join(COLS[:board.num_cols]))    
    print('')
      
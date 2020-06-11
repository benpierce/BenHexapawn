import naive 
import minimax 
import human 
from gamestate import GameState 
from board import Board
import hextypes
from utils import print_board, print_move, print_intro
import time 
import os 

def get_board_size():
    os.system('cls')  # on windows        
    while True:
        print('--------------------------------------------------------')
        print("Welcome to Ben Pierce's implementation of Hexapawn!")
        print("")
        print("Please choose a grid size (default 3x3)")
        print("   3) 3x3")
        print("   4) 4x4") 
        print("   5) 5x5")
        print('--------------------------------------------------------')
        board_size = input("Please enter a number between 3 and 5: ")   
        if board_size == "":    # Default to 3x3 if they just hit enter
            board_size = "3"
        
        if board_size not in ["3", "4", "5"]:
            os.system('cls')  # on windows        
            print("Error: {0} is not a valid choice. Try again".format(board_size))
            print("")
        else:
            break 

    return int(board_size)

def get_players():
    os.system('cls')  # on windows        
    while True:
        print('--------------------------------------------------------')
        print("Welcome to Ben Pierce's implementation of Hexapawn!")
        print("")
        print("Please choose play type")
        print("   1) Human vs Random Bot")
        print("   2) Human vs Minimax Bot")
        print("   3) Minimax Bot vs Random Bot")
        print('--------------------------------------------------------')
        player_types = input("Please enter a number between 1 and 3: ")   
        if player_types == "":    # Default to Human vs Minimax Bot if they just hit enter
            player_types = "1"
        
        if player_types not in ["1", "2", "3"]:
            os.system('cls')  # on windows        
            print("Error: {0} is not a valid choice. Try again".format(player_types))
            print("")
        else:
            break 

    white = ""
    black = ""

    if player_types == "1":
        return {
            hextypes.Player.white: human.Human(), 
            hextypes.Player.black: naive.RandomBot()          
        }, "Human", "Random"
    elif player_types == "2":
        return {
            hextypes.Player.white: human.Human(), 
            hextypes.Player.black: minimax.MinimaxBot()          
        }, "Human", "Minimax"
    elif player_types == "3":
        return {
            hextypes.Player.white: minimax.MinimaxBot(), 
            hextypes.Player.black: naive.RandomBot()          
        }, "Minimax", "Random"

def main():
    board_size = get_board_size()
    players, white, black = get_players()
    os.system('cls')
    turn = 0
    
    game = GameState.new_game(board_size, white, black) 
    print_intro(game.board)

    bot_move = None
    while not game.is_over():
        time.sleep(1) 

        turn = turn + 1
        print_board(game.board, turn, game.is_over(), game.next_player.other, bot_move)         
        bot_move = players[game.next_player].select_move(game)          
        game = game.apply_move(bot_move)                 

    print_board(game.board, turn, game.is_over(), game.next_player.other, bot_move)         
    winner = game.winner()
    print('%s Wins!!!' % (winner))

if __name__ == '__main__':
    main() 


import random 
from base import Agent 
from hextypes import Point 
from board import Move
from hextypes import Player 

# Based on the code from the book Deep Learning and the game of Go by Max Pumperla & Kevin Ferguson
# https://github.com/maxpumperla/deep_learning_and_the_game_of_go/blob/master/code/dlgo/minimax/alphabeta.py
class MinimaxBot(Agent):
    def __init__(self):
        self.MIN_SCORE = -999999
        self.MAX_SCORE = 999999
        self.max_depth = 3
        self.DEBUG = True

    def select_move(self, game_state):        
        best_moves = []
        best_score = None
        best_black = self.MIN_SCORE
        best_white = self.MIN_SCORE    

        # Loop over all legal moves.
        if self.DEBUG:
            print('---------------- MINIMAX DEBUG INFO --------------------')            
            print('Calculating scores for each possible move:')

        for possible_move in game_state.legal_moves():   
            # Calculate the game state if we select this move.
            next_state = game_state.apply_move(possible_move)
            
            # Since our opponent plays next, figure out their best
            # possible outcome from there.
            opponent_best_outcome = self.alpha_beta_result(
                next_state, self.max_depth,
                best_black, best_white,
                self.pawn_diff)

            # Our outcome is the opposite of our opponent's outcome.
            our_best_outcome = -1 * opponent_best_outcome

            if self.DEBUG:
                print('...{0} best outcome: {1}'.format(possible_move.name(), our_best_outcome))
            if (not best_moves) or our_best_outcome > best_score:
                # This is the best move so far.
                best_moves = [possible_move]
                best_score = our_best_outcome
                if game_state.next_player == Player.black:
                    best_black = best_score
                elif game_state.next_player == Player.white:
                    best_white = best_score
            elif our_best_outcome == best_score:
                # This is as good as our previous best move.
                best_moves.append(possible_move)

        if self.DEBUG:
            print('We have {0} best moves to choose from.'.format(len(best_moves)))
            print('--------------------------------------------------------')
            print('')

        if best_moves is None:
            return None                 
        
        # For variety, randomly select among all equally good moves.
        return random.choice(best_moves)

    def pawn_diff(self, game_state):
        # We care about how many pawns are on the board as well as how many legal moves there are available.
        black_pawns = game_state.get_pawn_count(Player.black)
        white_pawns = game_state.get_pawn_count(Player.white)

        black_forward_moves = game_state.get_legal_move_count(Player.black)
        white_forward_moves = game_state.get_legal_move_count(Player.white)

        diff = (black_pawns + black_forward_moves) - (white_pawns + white_forward_moves)

        if game_state.next_player == Player.black:
            return diff 
        return -1 * diff         

    def alpha_beta_result(self, game_state, max_depth, best_black, best_white, eval_fn):
        if game_state.is_over():                                               
            if game_state.winner() == game_state.next_player:      
                return self.MAX_SCORE                                   
            else:                  
                return self.MIN_SCORE                                   

        if max_depth == 0:                                         
            return eval_fn(game_state)                             

        best_so_far = self.MIN_SCORE
        for candidate_move in game_state.legal_moves():            
            next_state = game_state.apply_move(candidate_move)     
            opponent_best_result = self.alpha_beta_result(              
                next_state, max_depth - 1,                         
                best_black, best_white,                            
                eval_fn)                                           
            our_result = -1 * opponent_best_result                 

            if our_result > best_so_far:                           
                best_so_far = our_result                           

            if game_state.next_player == Player.white:
                if best_so_far > best_white:                       
                    best_white = best_so_far                       
                outcome_for_black = -1 * best_so_far               
                if outcome_for_black < best_black:                 
                    return best_so_far                             
            elif game_state.next_player == Player.black:
                if best_so_far > best_black:                      
                    best_black = best_so_far                       
                outcome_for_white = -1 * best_so_far               
                if outcome_for_white < best_white:                 
                    return best_so_far                             

        return best_so_far

# BenHexapawn
Welcome to my Hexapawn Implementation for Reinforcement Learning at UofT

**Note**: The Minimax implementation and some of the code structure of this Hexapawn implmentation were taken from the excellent book *Deep Learning and the Game of Go* written by *Max Pumperla* and *Kevin Ferguson*.

This code has been tested on Windows. To run, simply clone this repo and execute play.bat

## Configuration Options

When you initially start the game you'll be prompted to choose a grid size. 3x3 is the standard grid size for Hexapawn; however, in this implementation you can also choose 4x4 or 5x5 if you want to test yourself against the AI in a more complex scenario.

![Choosing Grid Size](img/screen1.png?raw=true "Choosing Grid Size")

Once you've settled on a grid size, you now have 3 options for competitive play:

![Completitive Play](img/screen2.png?raw=true "Competitive Play")

1. **Human vs Random Bot**: You play as a human (white) vs a bot that makes random moves (black). This opponent isn't very hard to beat, but serves as a good benchmark AI.

1. **Human vs Minimax Bot**: You play as a human (white) vs a bot (black) that uses a minimax with alpha-beta pruning AI. This opponent is considerably harder to beat, and in fact, should be unbeatable on a 3x3 grid. This bot uses a max_depth hyperparameter of 3, so it may be beatable on 4x4 or 5x5 grids, although it will still be very challenging.

1. **Minimax Bot vs Random Bot**: Sit back and enjoy a show as a minimax bot (white) battles it out with a bot that makes random moves (black). The minimax bot will crush the random bot each time.

## Playing as a Human

When the game first starts, you'll be playing as the white player, starting on the buttom row. The AI will be playing as the black player, starting on the top row.

To move one of your pawns, enter **sourcecell**:**destcell**. For instance, **A1**:**A2**. If you enter an invalid move, the program will notify you and you'll be prompted to enter a legal move.

You can resign at any time by typing *quit* as your move.

![How to Play](img/screen3.png?raw=true "How to Play")




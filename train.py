#! /usr/bin/python

import argparse
from board import board
from opponent import opponent
from move import move

def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
    else:
        turn = 'Red'
        pieces = gameboard.Red
    print 'It is '+turn+'\'s turn.'
    return turn, pieces


def progMove(pieces, prog):
    moveList = []

    for piece in pieces:
        moves = gameboard.getPieceMoves(piece)
        if moves:
            moveList.append((piece, moves))
            
    m = prog.move(moveList)
    m.pieces = pieces
    m.piece = gameboard.getPiece(pieces, m)

    if gameboard.checkMove(m) != True:
        gameboard.updatePiece(m)
    else:
        print 'not a valid move'

def trainGame():
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    print 'It is Red\'s turn.'

    while gameLoop:
        if turn == 'Red':
            progMove(pieces, trainee)
        else:
            progMove(pieces, trainer)

        gameboard.printBoard()
        turn, pieces = turns(turn)

        gameLoop = gameboard.win()


#parser = argparse.ArgumentParser(description='Input commands.')

#parser.add_argument('-color', default='Red', choices=['Red', 'Black'], help='Select a color you wish to play agaisnt the computer r or b')
#parser.add_argument('-load', default='y', choices=['y','n'], help='Load the last used program[y] or generate a new one[n]')
#add another argument for playing agaisnt the computer defaulting to yes


#then write a script that handles both so user can set up a game against the computer
        # or train the generated program
#args = vars(parser.parse_args())

gameboard = board("Red")

trainee = opponent('Red')
trainer = opponent('Black')


trainee.loadProgram()

trainer.genPieceProgram()
trainer.genMoveProgram()

trainGame()

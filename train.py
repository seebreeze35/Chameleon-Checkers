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

    if moveList != []:
        m = prog.move(moveList)
        m.pieces = pieces
        m.piece = gameboard.getPiece(pieces, m)
    
        if gameboard.checkMove(m) != True:
            gameboard.updatePiece(m)
        else:
            print 'not a valid move'
        return False
    else:
        return True

def trainGame():
    moveCount = 0
    winStatus = None
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    print 'It is Red\'s turn.'

    while gameLoop:

        if turn == 'Red':
            noMoves = progMove(pieces, trainee)
        else:
            noMoves = progMove(pieces, trainer)

        if noMoves == True:
            print turn + ' has no moves left. Game over.'
            if turn == 'Red':
                return 0
            else:
                return 1

        gameboard.printBoard()
        turn, pieces = turns(turn)
        gameboard.moveCount +=1
        if gameboard.moveCount == 60:
            print 'Draw'
            return 0
        gameLoop = gameboard.win()

gameboard = board("Red")

trainee = opponent('Red')
trainer = opponent('Black')


trainee.loadProgram()

trainer.genPieceProgram()
trainer.genMoveProgram()

winStatus =trainGame()
print winStatus

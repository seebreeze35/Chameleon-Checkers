#! /usr/bin/python

import argparse
from board import board
from opponent import opponent
from move import move

toLog=None

def log(statement):
    if toLog:
        print statement

def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
    else:
        turn = 'Red'
        pieces = gameboard.Red
    log('It is '+turn+'\'s turn.')
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
            log('not a valid move')
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
    log('It is Red\'s turn.')

    while gameLoop:

        if turn == 'Red':
            noMoves = progMove(pieces, trainee)
        else:
            noMoves = progMove(pieces, trainer)

        if noMoves == True:
            log(turn + ' has no moves left. Game over.')
            if turn == 'Red':
                return 0
            else:
                return 1

        gameboard.printBoard()
        turn, pieces = turns(turn)
        gameboard.moveCount +=1
        if gameboard.moveCount == 60:
            log('Draw')
            return 0
        gameLoop = gameboard.win()

parser = argparse.ArgumentParser(description='Input commands.')
parser.add_argument('-log', default='n', choices=['y','n'], help='Display output of the game?')

args = vars(parser.parse_args())

if args['log']=='y':
    toLog=True
else:
    toLog=False

gameboard = board("Red", toLog)

trainee = opponent('Red', toLog)
trainer = opponent('Black', toLog)


trainee.loadProgram()

trainer.genPieceProgram()
trainer.genMoveProgram()

for i in range(100):
    trainer.train()

winStatus =trainGame()
if winStatus == 0:
    print 'Red loses!'
    trainee.train() 
    log('trained')
else:
    print 'Red wins!'
    
trainee.saveProgram()

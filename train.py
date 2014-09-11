#! /usr/bin/python

import argparse
from core.board import board
from core.opponent import opponent
from core.move import move

toLog=None

def log(statement):
    if toLog:
        print(statement)

def checkForCaptures(pieceList):
    to_return = pieceList
    
    captureList = []

    for piece in pieceList:
        for _move in piece.moves:
            if _move.moveType == 2:
                captureList.append(piece)
                continue

    if captureList != []:
        to_return = captureList

    return to_return

def checkForMoves(pieceList):
    to_return = False

    for piece in pieceList:
        if piece.moves != []:
            to_return = True
            break

    return to_return

def score(red, black, winStatus):
    redScore = 10*len(red)
    blackScore = 15*len(black)
    winScore=0
    if winStatus == 1:
        winScore=100
    else:
        winScore=-100
    score = redScore-blackScore+winScore
    return score

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
    to_return = False
    pieceList = []

    for piece in pieces:
        hasValidMoves = piece.getPieceMoves()
        if hasValidMoves == True:
            pieceList.append(piece)

    if checkForMoves(pieceList) == True:
        pieceList = checkForCaptures(pieceList)

        _move = prog.move(pieceList)
        
        gameboard.updatePiece(_move)
        
        to_return = True
            
    return to_return

def trainGame():
    to_return = 0

    moveCount = 0
    winStatus = None
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    log('It is Red\'s turn.')

    while gameLoop:
        gameboard.printBoard()
        if turn == 'Red':
            validTurn = progMove(pieces, trainee)
        else:
            validTurn = progMove(pieces, trainer)

        if validTurn  == False:
            log(turn + ' has no moves left. Game over.')
            if turn == 'Red':
                to_return = 0
            else:
                to_return = 1
            break

        gameboard.moveCount +=1
        turn, pieces = turns(turn)

        if gameboard.moveCount == 60:
            log('Draw')
            to_return = 0
        gameLoop = gameboard.win()

    return to_return

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

winStatus =trainGame()

points = score(gameboard.Red, gameboard.Black, winStatus)

print points


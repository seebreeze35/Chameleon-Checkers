#! /usr/bin/python

import argparse
from core.board import board
from core.opponent import opponent
from core.move import move

def log(statement):
    print (statement)


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

def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
    else:
        turn = 'Red'
        pieces = gameboard.Red

    for piece in pieces:
        piece.hasCaptures = False

    log('It is '+turn+'\'s turn.')
    return turn, pieces

def playerMove(pieces):
    _move = move(gameboard, True)
    _move.pieces = pieces
    
    for piece in pieces:
        piece.getPieceMoves()
    
    while(_move.isValidMove == False):
        _move.getMove()
        
        #check to see if there is a valid capture move
        #forced player to make capture if one exists
        for piece in pieces:
            piece.getPieceMoves()
            if piece.hasCaptures == True and _move.moveType != 2:
                log("Must make capture move")
                _move.isValidMove = False
                _move.piece = None
    
    gameboard.updatePiece(_move)
    
def computerMove(pieces):
    pieceList = []
    
    for piece in pieces:
        hasValidMoves = piece.getPieceMoves()
        if hasValidMoves == True:
            pieceList.append(piece)

    pieceList = checkForCaptures(pieceList)
 
    _move = comp.move(pieceList)

    gameboard.updatePiece(_move)

def playerGame():
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    log('It is Red\'s turn.')

    while gameLoop:
        if turn == args['color']:
            gameboard.printBoard()
            playerMove(pieces)
        else:
            computerMove(pieces)

        
        turn, pieces = turns(turn)
        gameboard.moveCount +=1
        if gameboard.moveCount == 60:
            log('Draw')
            break
        gameLoop = gameboard.win()


parser = argparse.ArgumentParser(description='Input commands.')

parser.add_argument('-color', default='Red', choices=['Red', 'Black'], help='Select a color you wish to play agaisnt the computer r or b')
parser.add_argument('-load', default='y', choices=['y','n'], help='Load the last used program[y] or generate a new one[n]')

args = vars(parser.parse_args())


gameboard = board(args['color'], True)

if args['color']=='Red':
    comp = opponent('Black', True)
elif args['color']=='Black':
    comp = opponent('Red', True)

if args['load']=='y':
    comp.loadProgram()
else:
    comp.genPieceProgram()
    comp.genMoveProgram()
    comp.saveProgram()

comp.saveProgram()
playerGame()

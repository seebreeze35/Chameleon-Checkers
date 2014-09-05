#! /usr/bin/python

import argparse
from core.board import board
from core.opponent import opponent
from core.move import move

def log(statement):
    print (statement)

def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
        print len(gameboard.Black)
    else:
        turn = 'Red'
        pieces = gameboard.Red
    log('It is '+turn+'\'s turn.')
    return turn, pieces

def playerMove(pieces):
    _move = move(gameboard, True)
    _move.pieces = pieces
    while(_move.isValidMove == False):
        _move.getMove()
        
    gameboard.updatePiece(_move)
    
def computerMove(pieces):
    pieceList = []

    for piece in pieces:
        #piece.board = gameboard
        hasValidMoves = piece.getPieceMoves()
        if hasValidMoves == True:
            pieceList.append(piece)
#    print '-----'
 #   for m in moveList:
  #      for M in m[1]:
   #         print str(M.mX)+' '+str(M.mY)
   #x print '-----'

    _move = comp.move(pieceList)

    gameboard.updatePiece(_move)

def playerGame():
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    log('It is Red\'s turn.')

    while gameLoop:
        gameboard.printBoard()
        if turn == args['color']:
#            gameboard.printBoard()
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

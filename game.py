#! /usr/bin/python

import argparse
from board import board
from opponent import opponent
from move import move

def log(statement):
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

def playerMove(pieces):
    _move = move()
    _move.pieces = pieces
    moveInvalid = True
    while(moveInvalid):
        _move.getMove()
        moveInvalid = gameboard.checkMove(_move)
        
    gameboard.updatePiece(_move)

def computerMove(pieces):
    moveList = []

    for piece in pieces:
        moves = gameboard.getPieceMoves(piece)
        if moves:
            moveList.append((piece, moves))

#    print '-----'
 #   for m in moveList:
  #      for M in m[1]:
   #         print str(M.mX)+' '+str(M.mY)
   #x print '-----'
            
    m = comp.move(moveList)
    m.pieces = pieces
    m.piece = gameboard.getPiece(pieces, m)

    #if moveInvalid = gameboard.checkMove(piece, int(m[2]), int(m[3]))
    if gameboard.checkMove(m) != True:
        gameboard.updatePiece(m)
    else:
        log('not a valid move')

def playerGame():
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    log('It is Red\'s turn.')

    while gameLoop:
        if turn == args['color']:
            playerMove(pieces)
        else:
            computerMove(pieces)

        gameboard.printBoard()
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

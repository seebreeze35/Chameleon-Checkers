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

def playerMove(pieces):
    _move = move()
    _move.pieces = pieces
    _move.getMove()
    moveInvalid = gameboard.checkMove(_move)
    gameboard.updatePiece(_move)

def computerMove(pieces):
    validPieces = gameboard.getMovablePieces(comp.color)
    m = comp.move(validPieces, gameboard)
    m.pieces = pieces
    m.piece = gameboard.getPiece(pieces, m)

    #if moveInvalid = gameboard.checkMove(piece, int(m[2]), int(m[3]))
    if gameboard.checkMove(m) != True:
        gameboard.updatePiece(m)
    else:
        print 'not a valid move'

def playerGame():
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    print 'It is Red\'s turn.'

    while gameLoop:
        if turn == args['color']:
            playerMove(pieces)
        else:
            computerMove(pieces)

        gameboard.printBoard()
        turn, pieces = turns(turn)

        gameLoop = gameboard.win()


parser = argparse.ArgumentParser(description='Input commands.')

parser.add_argument('--color', default='Red', choices=['Red', 'Black'], help='Select a color you wish to play agaisnt the computer r or b')
#add another argument for playing agaisnt the computer defaulting to yes


#create another script for handling program training
#then write a script that handles both so user can set up a game against the computer
        # or train the generated program
args = vars(parser.parse_args())

gameboard = board(args['color'])

if args['color']=='Red':
    comp = opponent('Black')
elif args['color']=='Black':
    comp = opponent('Red')
playerGame()

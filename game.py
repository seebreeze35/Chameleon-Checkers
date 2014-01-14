#! /usr/bin/python

import argparse
from board import board


def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
    else:
        turn = 'Red'
        pieces = gameboard.Red

    print 'It is '+turn+'\'s turn.'

    return turn, pieces

def inputPiece(pieces):
    pieceInvalid = True
    while(pieceInvalid):
        print 'Input piece'
        x = raw_input("Select piece x: ")
        y = raw_input("Select piece y: ")
        pieceInvalid, piece = checkPiece(pieces, int(x), int(y))
    return piece

def inputMove():

    print 'Move to?'
    x = raw_input("Select x: ")
    y = raw_input("Select y: ")
    return x, y

def checkPiece(pieces, x, y):
    for piece in pieces:
        if piece.x == x and piece.y == y:
            return False, piece
    
    print 'Not valid please enter another piece.'
    return True, None


def playerGame():
#    gameboard = board(playerColor)
    
    gameboard.printBoard()
    
    gameLoop = True
    turn = 'Red'
    pieces = gameboard.Red
    print 'It is Red\'s turn.'

    while gameLoop:
        moveInvalid = True
        
        piece = inputPiece(pieces)
        
        while(moveInvalid):
            mx, my = inputMove()
            if mx == '' or my == '':
                piece = inputPiece(pieces)
                mx, my = inputMove()
            moveInvalid = gameboard.checkMove(piece, int(mx), int(my))
        gameboard.updatePiece(piece, int(mx), int(my))
        gameboard.printBoard()
        turn, pieces = turns(turn)

        gameLoop = gameboard.win()



parser = argparse.ArgumentParser(description='Input commands.')

parser.add_argument('--color', default='Red', choices=['Red', 'Black'], help='Select a color you wish to play agaisnt the computer r or b')
#add another argument for playing agaisnt the computer defaulting to yes

args = vars(parser.parse_args())

gameboard = board(args['color'])

playerGame()

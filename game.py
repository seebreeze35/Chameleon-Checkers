#! /usr/bin/python

from board import board

gameboard = board()

gameboard.printBoard()

gameLoop = True
turn = 'Red'
pieces = gameboard.Red
print 'It is Red\'s turn.'

def turns(turn):
    if turn == 'Red':
        turn = 'Black'
        pieces = gameboard.Black
    else:
        turn = 'Red'
        pieces = gameboard.Red

    print 'It is '+turn+'\'s turn.'

    return turn, pieces

def inputPiece():
    x = raw_input("Select piece x: ")
    y = raw_input("Select piece y: ")
    return x, y

def inputMove():
    print 'Move to?'
    x = raw_input("Select x: ")
    y = raw_input("Select y: ")
    return x, y

while gameLoop:
    moveInvalid = True
    
    inX, inY = inputPiece()
    
    for piece in pieces:
        x,y = piece.getPos()
        if int(inX) == x and int(inY) == y:
            while(moveInvalid):
                mx, my = inputMove()
                moveInvalid = gameboard.checkMove(piece, int(mx), int(my))
            gameboard.updatePiece(piece, int(mx), int(my))
            gameboard.printBoard()
            turn, pieces = turns(turn)
            break

    gameLoop = gameboard.win()



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
    print 'Input piece'
    x = raw_input("Select piece x: ")
    y = raw_input("Select piece y: ")
    return x, y

def inputMove():
    print 'Move to?'
    x = raw_input("Select x: ")
    y = raw_input("Select y: ")
    return x, y

def checkPiece(pieces, x, y):
    
    for piece in pieces:
        if piece.x == x and piece.y == y:
            return False, piece
            
    return True, None

while gameLoop:
    moveInvalid = True
    pieceInvalid = True

#need a smart way to get out of moving a piece if player no longer wishes to move said piece
    while(pieceInvalid):
        inX, inY = inputPiece()
        pieceInvalid, piece = checkPiece(pieces, int(inX), int(inY))

    x,y = piece.getPos()
    if int(inX) == x and int(inY) == y:
        while(moveInvalid):
            mx, my = inputMove()
            moveInvalid = gameboard.checkMove(piece, int(mx), int(my))
        gameboard.updatePiece(piece, int(mx), int(my))
        gameboard.printBoard()
        turn, pieces = turns(turn)

    gameLoop = gameboard.win()



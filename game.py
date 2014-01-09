#! /usr/bin/python

from board import board

gameboard = board()

gameboard.printBoard()

gameLoop = True

while gameLoop:
    move = None

    InputX = raw_input("Select piece x: ")
    InputY = raw_input("Select piece y: ")


    for piece in gameboard.Black:
        x,y = piece.getPos()
        if int(InputX) == x and int(InputY) == y:
            gameboard.updatePiece(piece)
            break
    gameboard.printBoard()

#    gameLoop = False

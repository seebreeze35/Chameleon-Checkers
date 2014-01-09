#! /usr/bin/python

from piece import piece
from space import space

#todo: create function to place pieces on the proper spaces
#      create a print out of the current board status
#      add ability to move a piece to another space
#      add rules based on piece type

class board:
    
    def __init__(self):
        self.name = 'Board'
        self.spaces = []
        self.Red = []
        self.Black = []
        self.setup()
        
    def setup(self):
        self.createSpaces()
        self.createPieces()
        self.setPieces()

    def createSpaces(self):
        for x in range(8):
            List = []
            for y in range(8):
                List.append(space(y,x))
            self.spaces.append(List)
        self.spaces.reverse()

    def createPieces(self):
        for ID in range(12):
            self.Red.append(piece('Red', ID))
            self.Black.append(piece('Black', ID))            

    def setPieces(self):
        redIter = 0
        blackIter = 0
        for row in range(8):
            if row < 3:
                for space in self.spaces[row]:
                    if space.color == 'Black':
                        space.setPiece(self.Black[blackIter])
                        blackIter+=1
            if row > 4:
                for space in self.spaces[row]:
                    if space.color == 'Black':
                        space.setPiece(self.Red[redIter])
                        redIter+=1


    def reset(self):
        self.setup()

    def getSpace(self, x, y):
        to_return = None
        for row in self.spaces:
            for space in row:
                if space.x == x and space.y == y:
                    to_return = space

        return to_return

    def updatePiece(self, piece):
        #this needs to be redone
        #I need error checking to make sure Im not going on top of another piece
        #also so that it does not go off the board
        #if so it needs to kick back and ask the player to redo the move
        x,y = piece.getPos()
        space = self.getSpace(x, y)
        space.piece = None
        if piece.color == 'Black':
            piece.move(-1)
        if piece.color == 'Red':
            piece.move(1)
        x,y = piece.getPos()
        print str(x)+' '+str(y) 
        space = self.getSpace(x,y)
        space.setPiece(piece)
        

    def updateBoard(self):
        for row in self.spaces:
            for space in row:
                space.checkPiece()
        
    def printBoard(self):
        count = 7
        for row in self.spaces:
            rowLines = ''
            for space in row:
                rowLines += space.printSpace()
            print str(count)+' '+rowLines
            count -=1
        print "   0  1  2  3  4  5  6  7 "

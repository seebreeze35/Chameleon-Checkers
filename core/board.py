#! /usr/bin/python

from piece import piece
from space import space
from move import move

#this needs to be a singleton
#each object needs to get a reference to it

class board:

    def __init__(self, color, log):
        self.name = 'Board'
        self.spaces = []
        self.Red = []
        self.Black = []
        self.blackDirection = None
        self.redDirection = None
        self.playerColor = color
        self.moveCount = 0
        self.tolog=log
        self.setup()
        
    def setup(self):
        self.createSpaces()
        self.createPieces()
        self.setPieces()

    def log(self, statement):
        if self.tolog:
            print(statement)

    def reset(self):
        self.setup()

    def createSpaces(self):
        for x in range(8):
            List = []
            for y in range(8):
                List.append(space(y,x))
            self.spaces.append(List)
        self.spaces.reverse()

    def createPieces(self):
        for ID in range(12):
            self.Red.append(piece('Red', ID, self))
            self.Black.append(piece('Black', ID, self))           

    def setPieces(self):
        redIter = 0
        blackIter = 0

        def fillRow(row, Iter, color):
            for space in self.spaces[row]:
                if space.color == 'Black':
                    if color == 'Red':
                        space.setPiece(self.Red[Iter])
                        Iter +=1
                    else:
                        space.setPiece(self.Black[Iter])
                        Iter +=1
            return Iter

        if self.playerColor == 'Black':  
            for row in range(8):
                if row < 3:
                    redIter = fillRow(row, redIter, 'Red')
                    self.redDirection = 'Down'
                elif row > 4:
                    blackIter = fillRow(row, blackIter, 'Black') 
                    self.blackDirection = 'Up'
        elif self.playerColor == 'Red':
            for row in range(8):
                if row < 3:
                    blackIter = fillRow(row, blackIter, 'Black')
                    self.blackDirection = 'Down'
                elif row > 4:
                    redIter = fillRow(row, redIter, 'Red')
                    self.redDirection = 'Up'

    def getPiece(self, x, y):
        to_return = None
        
        pieces = self.Red + self.Black
        for piece in pieces:
            if piece.x == x and piece.y == y:
                to_return = piece

        return to_return

    def getSpace(self, x, y):
        #input assumes type is int
        to_return = None
        for row in self.spaces:
            for space in row:
                if space.x == x and space.y == y:
                    to_return = space

        return to_return

    def spaceTaken(self, x, y):
        #True means space is taken
        #False means there is no piece on given space
        to_return = True

        space_to_check = self.getSpace(x,y)
        if space_to_check != None:
            if space_to_check.piece == None:
                to_return = False

        return to_return

    def removePiece(self, piece):
        #Todo improve this
        try:
            self.Black.remove(piece)
        except:
            try:
                self.Red.remove(piece)
            except:
                self.log('Fatal error removing piece')

        
    def updatePiece(self, _move):
        if _move.moveType == 1:
            self._regMove(_move)
        elif _move.moveType == 2:
            self._captureMove(_move)

        return self

    def _regMove(self,_move):
        selectedSpace = self.getSpace(_move.inX, _move.inY)
        moveSpace = self.getSpace(_move.mX, _move.mY)
        _move.piece.move(_move.mX, _move.mY)
        moveSpace.setPiece(_move.piece)
        selectedSpace.piece = None

    def _captureMove(self, _move):
        selectedSpace = self.getSpace(_move.inX, _move.inY)
        moveSpace = self.getSpace(_move.mX, _move.mY)
        spaceBetween = _move.getSpaceBetween()
        self.removePiece(spaceBetween.piece)
        _move.piece.move(_move.mX, _move.mY)
        moveSpace.setPiece(_move.piece)
        self.log("Captured "+spaceBetween.piece.color+' '+str(spaceBetween.piece.id))
        spaceBetween.piece = None
        selectedSpace.piece = None

    def updateBoard(self):
        for row in self.spaces:
            for space in row:
                space.checkPiece()
        
    def printBoard(self):
        count = 7
        if self.tolog:
            for row in self.spaces:
                rowLines = ''
                for space in row:
                    rowLines += space.printSpace()
                print (str(count)+' '+rowLines)
                count -=1
            self.log("   0  1  2  3  4  5  6  7 ")

    def win(self):
        if len(self.Black)==0:
            self.log('Red wins!')
            return False
        elif len(self.Red)==0:
            self.log('Black wins!')
            return False
        else:
            return True


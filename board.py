#! /usr/bin/python

from piece import piece
from space import space

class board:
    
    def __init__(self, color):
        self.name = 'Board'
        self.spaces = []
        self.Red = []
        self.Black = []
        self.blackDirection = None
        self.redDirection = None
        self.playerColor = color
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

    def reset(self):
        self.setup()

    def getSpace(self, x, y):
        #input assumes type is int
        to_return = None
        for row in self.spaces:
            for space in row:
                if space.x == x and space.y == y:
                    to_return = space
        return to_return

    def getSpaceBetween(self, _move):
        to_return = None

        if _move.mX > _move.piece.x:
            if _move.mY > _move.piece.y:
                to_return = self.getSpace(_move.mX-1, _move.mY-1)
            elif _move.inY < _move.piece.y:
                to_return = self.getSpace(_move.mY-1, _move.mY+1)
        elif _move.mX < _move.piece.x:
            if _move.mY > _move.piece.y:
                to_return = self.getSpace(_move.mX+1, _move.mY-1)
            elif _move.mY < _move.piece.y:
                to_return = self.getSpace(_move.mX+1, _move.mY+1)
        return to_return

    def removePiece(self, piece):
        try:
            self.Black.remove(piece)
        except:
            try:
                self.Red.remove(piece)
            except:
                print 'Fatal error removing piece'

    def checkCapture(self, _move):
        spaceBetween = self.getSpaceBetween(_move)
        
        if spaceBetween.piece == None or spaceBetween.piece.color == _move.piece.color:
            print 'Not a valid move!'
            return True
        else:
            print 'Captured '+spaceBetween.piece.color+' '+str(spaceBetween.piece.id)
            self.removePiece(spaceBetween.piece)
            spaceBetween.piece = None
            return False
    
    def checkForward(self, _move):

        def forward(m):
            if m.mY > m.piece.y:
                return False
            else:
                print 'Not a valid move!'
                return True
        def backward(m):
            if m.mY < m.piece.y:
                return False
            else:
                print 'Not a valid move!'
                return True

        if _move.piece.color == 'Red':
            if self.redDirection == 'Up':
                return forward(_move)
            else:
                return backward(_move)
        elif _move.piece.color == 'Black':
            if self.blackDirection == 'Up':
                return forward(_move)
            else:
                return backward(_move)

    #Todo this is big probably need to refactor this down to be easier to read
    def checkMove(self, _move):
        #True is bad 
        #False is good
        to_return = None
        space = self.getSpace(_move.mX, _move.mY)
        if space.piece == None:
            if space.color != 'Black':
                print 'Space not black!'
                to_return = True
            #check change in column
            elif _move.mX == _move.piece.x:
                print 'Not a valid move!'
                to_return = True
            #check if a valid capture move
            elif abs(_move.mX-_move.piece.x)%2 == 0:
                to_return = self.checkCapture(_move)
            elif abs(_move.mX-_move.piece.x)>1:
                if abs(_move.mX-_move.piece.x)%2==1:
                    print 'Not a valid move!'
                    to_return = True
            elif _move.piece.Type != 'King':
                to_return = self.checkForward(_move)
            else:
                to_return = False
        else:
            print 'Space occupied!'
            to_return = True

        if to_return == False:
            if _move.mY == 7 or _move.mY == 0:
                _move.piece.King()

        return to_return

    def updatePiece(self, _move):
        #this probably needs to be redone
        #x,y = piece.getPos()
        space = self.getSpace(_move.inX, _move.inY)
        space.piece = None
        _move.piece.move(_move.mX, _move.mY)
#        x,y = piece.getPos()
        space = self.getSpace(_move.mX, _move.mY)
        space.setPiece(_move.piece)
        

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

    def win(self):
        if len(self.Black)==0:
            print 'Red wins!'
            return False
        elif len(self.Red)==0:
            print 'Black wins!'

            return False
        else:
            return True

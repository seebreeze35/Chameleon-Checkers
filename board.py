#! /usr/bin/python

from piece import piece
from space import space

#todo:  add rules based on piece type
#       check for valid moves


class board:
    
    def __init__(self):
        self.name = 'Board'
        self.spaces = []
        self.Red = []
        self.Black = []
        self.blackDirection = None
        self.redDirection = None
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
                    
        input = raw_input('Pick color (R or B): ')
        input = input[:1]
        if input == 'B' or input == 'b':
            for row in range(8):
                if row < 3:
                    redIter = fillRow(row, redIter, 'Red')
                    self.redDirection = 'Down'
                elif row > 4:
                    blackIter = fillRow(row, blackIter, 'Black') 
                    self.blackDirection = 'Up'
        elif input == 'R' or input == 'r':
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

    def getSpaceBetween(self, piece, x, y):
        to_return = None

        if x > piece.x:
            if y > piece.y:
                to_return = self.getSpace(x-1, y-1)
            elif y < piece.y:
                to_return = self.getSpace(x-1, y+1)
        elif x < piece.x:
            if y > piece.y:
                to_return = self.getSpace(x+1, y-1)
            elif y < piece.y:
                to_return = self.getSpace(x+1, y+1)
        return to_return

    def removePiece(self, piece):
        try:
            self.Black.remove(piece)
        except:
            try:
                self.Red.remove(piece)
            except:
                print 'Fatal error removing piece'

    def checkCapture(self, piece, mx, my):
        spaceBetween = self.getSpaceBetween(piece, mx, my)
        
        if spaceBetween.piece == None or spaceBetween.piece.color == piece.color:
            print 'Not a valid move!'
            return True
        else:
            print 'Captured '+spaceBetween.piece.color+' '+str(spaceBetween.piece.id)
            self.removePiece(spaceBetween.piece)
            spaceBetween.piece = None
            return False
    
    def checkForward(self, piece, my):

        def forward(piece, my):
            if my > piece.y:
                return False
            else:
                print 'Not a valid move!'
                return True
        def backward(piece, my):
            if my < piece.y:
                return False
            else:
                print 'Not a valid move!'
                return True

        if piece.color == 'Red':
            if self.redDirection == 'Up':
                return forward(piece, my)
            else:
                return backward(piece, my)
        elif piece.color == 'Black':
            if self.blackDirection == 'Up':
                return forward(piece, my)
            else:
                return backward(piece, my)

    #Todo this is big probably need to refactor this down to be easier to read
    def checkMove(self, piece, mx, my):
        #True is bad 
        #False is good
        to_return = None
        space = self.getSpace(mx, my)
        if space.piece == None:
            if space.color != 'Black':
                print 'Space not black!'
                to_return = True
            #check change in column
            elif mx == piece.x:
                print 'Not a valid move!'
                to_return = True
            #check if a valid capture move
            elif abs(mx-piece.x)%2 == 0:
                to_return = self.checkCapture(piece, mx, my)
            elif abs(mx-piece.x)>1:
                if abs(mx-piece.x)%2==1:
                    print 'Not a valid move!'
                    to_return = True
            elif piece.Type != 'King':
                to_return = self.checkForward(piece, my)
            else:
                to_return = False
        else:
            print 'Space occupied!'
            to_return = True

        if to_return == False:
            if my == 7 or my == 0:
                piece.King()

        return to_return

    def updatePiece(self, piece, mx, my):
        #this probably needs to be redone
        x,y = piece.getPos()
        space = self.getSpace(x, y)
        space.piece = None
        piece.move(mx, my)
        x,y = piece.getPos()
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

    def win(self):
        if len(self.Black)==0:
            print 'Red wins!'
            return False
        elif len(self.Red)==0:
            print 'Black wins!'

            return False
        else:
            return True

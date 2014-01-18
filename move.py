#! /usr/bin/python

class move:
    def __init__(self):
        self.inX = None
        self.inY = None
        self.mX = None
        self.mY = None
        self.piece = None
        self.pieces = None

    @classmethod
    def altInit(self, x, y):
        self.inX = x
        self.inY = y
        self.inputMove()

    def inputPiece(self):
        #add error handling to prevent crash from not having a x or y value
        pieceInvalid = True
        while(pieceInvalid):
            print 'Input piece'
            self.inX = raw_input("Select piece x: ")
            self.inY = raw_input("Select piece y: ")
            self.inX = int(self.inX)
            self.inY = int(self.inY)
            pieceInvalid = self.checkPiece()

    def inputMove(self):
        print 'Move to?'
        self.mX = raw_input("Select x: ")
        self.mY = raw_input("Select y: ")
        self.mX = int(self.mX)
        self.mY = int(self.mY)

    def checkPiece(self):
        for piece in self.pieces:
            if piece.x == self.inX and piece.y == self.inY:
                self.piece = piece
                return False
    
        print 'Not valid please enter another piece.'
        return True

    def getMove(self):            
        #this is for player piece selection
        #todo: need a way to undo a piece selection
        self.inputPiece()
        self.inputMove()

    def setMove(self, inX, inY, mX, mY):
        self.inX = int(inX)
        self.inY = int(inY)
        if self.checkPiece() != False:
            print 'computer failed'
            
        self.mX = int(mX)
        self.mY = int(mY)
    
#todo:        
#log
#do I want this to be destroyed after its completed?

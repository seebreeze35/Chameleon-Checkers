#! /usr/bin/python

class move:
    def __init__(self, pieces):
        self.inputX = None
        self.inputY = None
        self.moveX = None
        self.moveY = None
        self.piece = None
        self.pieces = pieces

    def inputMove(self):
        print 'Move to?'
        self.inputX = raw_input("Select x: ")
        self.inputY = raw_input("Select y: ")

    def checkPiece(self):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                self.piece = piece
                return False
    
        print 'Not valid please enter another piece.'
        return True

    def getMove(self):
        moveCheck = True
        while(moveCheck):
            self.inputMove()
            moveCheck = self.checkPiece()
        
#get where user wants it moved to
#check validity
#log
#do I want this to be destroyed after its completed?

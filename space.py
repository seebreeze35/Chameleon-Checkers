#! /usr/bin/python

class space:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None
        self.piece = None
        self.getSpaceColor()
    
    def getSpaceColor(self):
        mod_val = (self.x + self.y)%2
        if mod_val == 0:
            self.color = 'Black'
        else:
            self.color = 'White'

    def setPiece(self, piece):
        self.piece = piece
        self.piece.setCurrentPos(self.x, self.y)

    def checkPiece(self):
        if self.piece != None:
            x, y = self.piece.getPos()
            if self.x != x or self.y != y:
                print 'todo'
        
    def printSpace(self):
        if self.piece !=None:
            return '['+self.piece.color[:1]+']'
        else:
            return '[ ]'

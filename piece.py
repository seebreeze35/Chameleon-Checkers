#! /usr/bin/python

class piece:
    
    def __init__(self,color, ID):
        #number
        self.id = ID
        self.color = color
        self.inPlay = True
        self.x = None
        self.y = None
        self.Type = 'Regular'
        
    def getPos(self):
        return self.x, self.y

    def checkStatus(self):
        print self.inPlay
        print str(self.x) +' '+str(self.y)
        
    def setCurrentPos(self, x, y):
        self.x = x
        self.y = y        

    def move(self, x, y):
        self.x = x
        self.y = y

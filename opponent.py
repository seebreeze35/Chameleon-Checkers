#! /usr/bin/python
from move import move
import ai, cloud, pickle

class opponent:
    def __init__(self, color):
        self.id = 0
        self.color = color
        self.pieceProgram = None
        self.moveProgram = None
        self.genPieceProgram()
        self.genMoveProgram()

    def move(self, validPieces):
        pieceMax, moveMax = None, None
        pieceIndex = None
        p, m = None, None

        for valid in validPieces:
            #print str(valid[0].x)  +' '+str(valid[0].y) 
            num = self.pieceProgram.evaluate([valid[0].x, valid[0].y])
            if num >pieceMax or pieceMax == None:
                pieceMax = num
                p = valid[0]
                pieceIndex = valid

        for valid in pieceIndex[1]:
            print str(valid.mX)  +' '+str(valid.mY)
            num = self.moveProgram.evaluate([valid.mX, valid.mY])
            if num >moveMax or moveMax == None:
                moveMax = num
                m = valid

        print 'Piece: '+str(p.x)+' '+str(p.y)
        print 'Move: '+str(m.mX)+' '+str(m.mY)

        return m

    def genPieceProgram(self):
        size = False
        while (size == False):
            program = ai.makerandomtree(2)
            size = ai.getSize(program)
        self.pieceProgram = program

    def genMoveProgram(self):
        size = False
        while (size == False):
            program = ai.makerandomtree(2)
            size = ai.getSize(program)
        self.moveProgram = program

    
    def saveProgram(self):
        f = open('Piece.pickle', 'w')
        blob = cloud.serialization.cloudpickle.dump(self.pieceProgram,f)
        f.close()

        f = open('Move.pickle', 'w')
        blob = cloud.serialization.cloudpickle.dump(self.moveProgram,f)
        f.close()
    
    def loadProgram(self):
        self.pieceProgram = pickle.load(open("Piece.pickle", "rb"))
        self.moveProgram = pickle.load(open("Move.pickle", "rb"))

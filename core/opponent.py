#! /usr/bin/python
from move import move
import ai
import cloud, pickle

class opponent:
    def __init__(self, color, log):
        self.id = 0
        self.color = color
        self.pieceProgram = None
        self.moveProgram = None
        self.toLog = log

    def log(self,statement):
        if self.toLog:
            print(statement)


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
            #self.log(str(valid.mX)  +' '+str(valid.mY))
            num = self.moveProgram.evaluate([valid.mX, valid.mY])
            if num >moveMax or moveMax == None:
                moveMax = num
                m = valid

        self.log('Piece: '+str(p.x)+' '+str(p.y))
        self.log('Move: '+str(m.mX)+' '+str(m.mY))

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

    def train(self):
        #self.pieceProgram = ai.crossover(self.pieceProgram, trainer.pieceProgram)
        #self.moveProgram = ai.crossover(self.moveProgram, trainer.moveProgram)
        self.pieceProgram = ai.mutate(self.pieceProgram,2)
        self.moveProgram = ai.mutate(self.moveProgram,2)
    
    def saveProgram(self):
        f = open('core/Piece.pickle', 'w')
        blob = cloud.serialization.cloudpickle.dump(self.pieceProgram,f)
        f.close()

        f = open('core/Move.pickle', 'w')
        blob = cloud.serialization.cloudpickle.dump(self.moveProgram,f)
        f.close()
    
    def loadProgram(self):
        self.pieceProgram = pickle.load(open("core/Piece.pickle", "rb"))
        self.moveProgram = pickle.load(open("core/Move.pickle", "rb"))

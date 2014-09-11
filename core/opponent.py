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
        selectedPiece = None
        p, m = None, None

        for valid in validPieces: 
            num = self.pieceProgram.evaluate([valid.x, valid.y])
            if num >pieceMax or pieceMax == None:
                pieceMax = num
                p = valid
                selectedPiece = valid

        for move in selectedPiece.moves:
            num = self.moveProgram.evaluate([move.mX, move.mY])
            if num >moveMax or moveMax == None:
                moveMax = num
                m = move

        self.log('Piece: '+str(m.inX)+' '+str(m.inY))
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

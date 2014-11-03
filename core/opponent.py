#! /usr/bin/python
from move import move
import ai

class opponent:
    def __init__(self, color, seed, log):
        self.id = 0
        self.color = color
        self.pieceProgram = None
        self.moveProgram = None
        self.toLog = log
        self.seed = seed

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
        self.seed.setParsable(self.seed.pieceSeed)
        program = ai.makeTree(self.seed)
        self.pieceProgram = program

    def genMoveProgram(self):
        size = False
        self.seed.setParsable(self.seed.moveSeed)
        program = ai.makeTree(self.seed)
        self.moveProgram = program

    def train(self):
        #self.pieceProgram = ai.crossover(self.pieceProgram, trainer.pieceProgram)
        #self.moveProgram = ai.crossover(self.moveProgram, trainer.moveProgram)
        self.pieceProgram = ai.mutate(self.pieceProgram,2)
        self.moveProgram = ai.mutate(self.moveProgram,2)

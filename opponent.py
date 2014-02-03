#! /usr/bin/python
from move import move
import ai

class opponent:
    def __init__(self, color):
        self.id = 0
        self.color = color
        self.pieceProgram = None
        self.moveProgram = None
        self.genPieceProgram()
        self.genMoveProgram()
#        print self.pieceProgram.display()
        print self.moveProgram.display()

    #need to generate a move program
    #get a list of valid moves from the give piece
    #create the move from the moce program

    def move(self, validPieces, board):
        pieceMax, moveMax = None, None
        p, m = None, None

        for valid in validPieces:
           # print str(valid.x)  +' '+str(valid.y)
            num = self.pieceProgram.evaluate([valid.x, valid.y])
            if num >pieceMax or pieceMax == None:
                pieceMax = num
                p = valid

        validMoves = board.getPieceMoves(p)

#        print 'moves'
 #       for valid in validMoves:
  #          print str(valid.mX)+' '+str(valid.mY)

        for valid in validMoves:
           # print str(valid.x)  +' '+str(valid.y)
            num = self.moveProgram.evaluate([valid.mX, valid.mY])
            if num >moveMax or moveMax == None:
                moveMax = num
                m = valid

        print 'moves--'
        for valid in validMoves:
            print str(valid.mX)+' '+str(valid.mY)

        print 'Piece: '+str(p.x)+' '+str(p.y)
        print 'Move: '+str(m.mX)+' '+str(m.mY)

#        _move = move()
 #       _move.inX = m.x
  #      _move.inY = m.y
   #     _move.inputMove()
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

    

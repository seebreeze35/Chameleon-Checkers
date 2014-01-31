#! /usr/bin/python
from move import move
import ai

class opponent:
    def __init__(self, color):
        self.id = 0
        self.color = color
        self.program = None
        self.genPieceProgram()
        print self.program.display()

    #need to generate a move program
    #get a list of valid moves from the give piece
    #create the move from the moce program

    def move(self, validMoves, board):
        moveMax = None
        m = None

        for valid in validMoves:
           # print str(valid.x)  +' '+str(valid.y)
            num = self.program.evaluate([valid.x, valid.y])
           # print num
            if num >moveMax or moveMax == None:
                moveMax = num
                m = valid

        validMoves = board.getPieceMoves(m)

        print str(m.x)+' '+str(m.y)

        _move = move()
        _move.inX = m.x
        _move.inY = m.y
        _move.inputMove()
        return _move

    def genPieceProgram(self):
        size = False
        while (size == False):
            program = ai.makerandomtree(2)
            size = ai.getSize(program)
        self.program = program

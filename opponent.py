#! /usr/bin/python
from move import move
import ai

class opponent:
    def __init__(self, color):
        self.id = 0
        self.color = color
        self.program = ai.makerandomtree(2)#ai.exampletree()
        print self.program.display()


    def move(self, validMoves):
        m = validMoves[-1]
        print str(m.x)+' '+str(m.y)

        _move = move()
        _move.inX = m.x
        _move.inY = m.y
        _move.inputMove()
        return _move

    

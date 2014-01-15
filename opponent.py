#! /usr/bin/python



class opponent:
    def __init__(self):
        self.id = 0
        self.moves = [(1,5,2,4),(2,4,0,2),(3,5,2,4)]

    def move(self):
        #initial set up of an opponent object moves are scripted to simulate what the computer would do
        #assumes player is using red pieces
        return self.moves.pop()
    

    
    

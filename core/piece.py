#! /usr/bin/python

from move import move

#need to allow checking of valid king moves
#they might be created already but the computer has not done anything 
#with a king yet

class piece:
    
    def __init__(self,color, ID, board):
        #number
        self.id = ID
        self.color = color
        self.inPlay = True
        self.x = None
        self.y = None
        self.Type = 'Regular'
        self.moves = []
        self.board = board
        self.hasCaptures = False
        
    def getPos(self):
        return self.x, self.y

    def checkStatus(self):
        print(self.inPlay)
        print(str(self.x) +' '+str(self.y))
        
    def setCurrentPos(self, x, y):
        self.x = x
        self.y = y        

    def move(self, x, y):
        self.x = x
        self.y = y

    def clean(self):
        self.hasCaptures = False
        self.moves = []

    def King(self):
        self.Type = 'King'        

    def getPieceMoves(self):
        direction = None

        self.clean()

        if self.Type == 'Regular':
            if self.color == 'Red':
                direction = self.board.redDirection
            else:
                direction = self.board.blackDirection
            
            self.moves = self._checkDirection(direction)

        else:
            #king check
            #check move Up
            temp = self._checkDirection('Up')
            if temp:
                for m in temp:
                    self.moves.append(m)
            #check move Down
            temp = self._checkDirection('Down')
            if temp:
                for m in temp:
                    self.moves.append(m)
                    
        to_return = False

        if self.moves != []:
            to_return = True
            self.checkForJumps()
            
        return to_return

    def _checkDirection(self, direction):
        moveList = []
        #check move
        m1, m2, = self._directionMoveCheck(direction)
        if m1:
            moveList.append(m1)
        if m2:
            moveList.append(m2)

        #check capture
        #check if theres an opposing piece in the next spot?
        m1, m2 = self._directionJumpCheck(direction)
        if m1:
            moveList.append(m1)
        if m2:
            moveList.append(m2)

        return moveList

    def checkForJumps(self):
        #This checks for any jump moves if so it returns only a list 
        #of jumps
        moves = filter(lambda m: m.moveType == 2, self.moves)
        if moves != []:
            self.moves = moves
            self.hasCaptures = True

    def _directionMoveCheck(self, direction):
        if direction == 'Down':
            mY = self.y-1
        else:
            mY = self.y+1

        mX = self.x+1
        m1 = self._createMove(mX, mY)

        mX = self.x-1
        m2 = self._createMove(mX, mY)

        return m1, m2

    def _checkRanges(self, x, y):
        to_return = True

        if x > 7 or x < 0:
            to_return = False
        if y > 7 or y < 0:
            to_return = False

        return to_return

    def _directionJumpCheck(self, direction):
        m1, m2 = None, None

        def checkJump(x):
            to_return = None
            if self.board.spaceTaken(x, y)==True and self._checkRanges(X, Y):
                if self.board.spaceTaken(X, Y)!=True:
                    to_return  = self._createMove(X, Y)
            return to_return

        if direction == 'Down':
            Y = self.y-2
            y = Y+1
        else:
            Y = self.y+2
            y = Y-1

        X = self.x+2
        m1 = checkJump(self.x+1)

        X = self.x-2
        m2 = checkJump(self.x-1)

        return m1, m2

    def _createMove(self, x, y):
        to_return = None
        if self._checkRanges(self.x, self.y) and self._checkRanges(x,y):
            if self.x != x and self.y != y:
                _move = move(self.board, False)
                _move.noInputInit(self.x, self.y, self)
                _move.setMove(x,y)
                _move.checkMove()
                if _move.isValidMove:
                    to_return = _move

        return to_return

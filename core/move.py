#! /usr/bin/python


#player cannot capture opponents piece
#piece doesnt check if the move space has a piece

regMove = 1
jumpMove = 2

class move:
    import board
    
    def __init__(self, board, toLog):
        self.inX = None
        self.inY = None
        self.mX = None
        self.mY = None
        self.piece = None
        self.board = board
        self.isValidMove = False
        self.moveType = None
        self.toLog = toLog

    def log(self, statement):
        if self.toLog == True:
            print(statement)

    #needs to be alt constructor
    def noInputInit(self, x, y, piece):
        self.mX = x
        self.mY = y
        self.piece = piece
        self.inX = piece.x
        self.inY = piece.y
        self.board = piece.board
        self.isValidMove = False

    def inputPiece(self):
        to_return = False
        while(self.piece == None):
#            print('Input piece')
            _in = raw_input("Piece xy: ")
            try:
                self.inX = int(_in[0])
                self.inY = int(_in[1])
                to_return = True
            except:
                self.log("Invald entry only numbers 0-9 are accepted")
                self.inputPiece()
            self.piece = self.board.getPiece(self.inX, self.inY)
        return to_return

    def inputMove(self):
        to_return = False
        while self.isValidMove==False:
            _in = raw_input("Move to space xy: ")
            try:
                self.mX = int(_in[0])
                self.mY = int(_in[1])
                to_return = True
            except:
                if len(_in)==0:
                    self.piece = None
                    self.getMove()
                else:
                    self.log("Invald entry only numbers 0-9 are accepted")
            if to_return == True:
                self.isValidMove = self.checkMove()
        return to_return

    def setMove(self, x, y):
        self.mX = x
        self.mY = y

    def getMove(self):            
        pieceValid = self.inputPiece()
        moveValid = self.inputMove()

    def checkMove(self):
        #True is bad 
        #False is good
        to_return = None

        space = self.board.getSpace(self.mX, self.mY)
        if self.board.spaceTaken(self.mX, self.mY) == False:
            if space.color != 'Black':
                self.log('Space not black!')
                to_return = False
            #check change in column
            elif self.mX == self.piece.x:
                self.log('Not a valid move!1')
                to_return = False
            #check if a valid capture move
            elif abs(self.mX-self.piece.x)%2 == 0:
                if self.inX != self.mX and self.inY != self.mY: 
                    to_return = self.checkCapture()
                else:
                    self.log('Not a valid move!1')
                    return False
            elif abs(self.mX-self.piece.x)>1:
                if abs(self.mX-self.piece.x)%2==1:
                    self.log('Not a valid move!2')
                    to_return = False
            elif self.piece.Type != 'King':
                to_return = self.checkAdvance()
            #Todo this is a check for king moves
            else:
                print 'King move check'
                to_return = True           
        else:
            self.log('Space occupied!')
            to_return = False
            
        if self.mY == 7 or self.mY == 0:
            print 'king'
            self.piece.King()
            to_return = True
            
        self.isValidMove = to_return

        if self.moveType != jumpMove:
            self.moveType = regMove

        return to_return

    def checkAdvance(self):

        def forward(self):
            if self.mY > self.piece.y:
                return self.checkMoveRange()

        def backward(self):
            if self.mY < self.piece.y:
                return self.checkMoveRange()

        if self.piece.color == 'Red':
            if self.board.redDirection == 'Up':
                return forward(self)
            else:
                return backward(self)
        elif self.piece.color == 'Black':
            if self.board.blackDirection == 'Up':
                return forward(self)
            else:
                return backward(self)

    def checkMoveRange(self):
        if abs(self.mY - self.piece.y) == 1:
            return True
        else:
            self.log('Not a valid move!5')
            return False    

    def checkCapture(self):
        spaceBetween = self.getSpaceBetween()
        if spaceBetween.piece == None or spaceBetween.piece.color == self.piece.color:
            self.log('Not a valid move!6')
            return False
        else:
            self.moveType = jumpMove
            self.board.moveCount = 0
            return True

    def getSpaceBetween(self):
        to_return = None

        def check(self, x):
            to_return = None
            if self.mY > self.piece.y:
                to_return = self.board.getSpace(x, self.mY-1)
            elif self.mY < self.piece.y:
                to_return = self.board.getSpace(x, self.mY+1)
            return to_return

        if self.mX > self.piece.x:
            to_return = check(self, self.mX-1)
        elif self.mX < self.piece.x:
            to_return = check(self, self.mX+1)
        return to_return

#todo:        
#log moves into file
#do I want this to be destroyed after its completed?

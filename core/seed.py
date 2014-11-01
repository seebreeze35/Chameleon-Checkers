#! /usr/bin/python

import random
import string
import base64
import hashlib

class seed:
    def __init__(self, val):
        if val != None:
            self.seed = val
        else:
            self.seed = self.randomSeed()
        print 'Seed: '+ str(self.seed)
        self.pieceSeed = base64.b64encode(self.seed)
        self.moveSeed = base64.b32encode(self.seed)
        self.parsedSeed = self.pieceSeed
        self.originalParsable = self.parsedSeed
            
    def randomSeed(self):
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(15))

    def getSeed(self):
        return self.pieceSeed

    def getParsableSeed(self):
        return self.parsedSeed

    def setParsableSeed(self, seed):
        self.parsedSeed = seed

    def setParsable(self, val):
        self.parsedSeed = val
        self.originalParsable = val

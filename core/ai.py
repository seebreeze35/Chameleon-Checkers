#! /usr/bin/python

from random import random, randint, choice
from copy import deepcopy
from math import log

import json
import subprocess

import string

from core.seed import seed

class fwrapper:
    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name

class node:
    def __init__(self, fw, children, char):
        self.function = fw.function
        self.name = fw.name
        self.children = children
        self.size = 0
        self.char = char

    def evaluate(self, inp):
        results = [n.evaluate(inp) for n in self.children]
        return self.function(results)

    def display(self, indent=0):
        print (' '*indent)+self.name
        for c in self.children:
            c.display(indent+1)
        
    def getSize(self):
        for c in self.children:
            self.size += c.getSize()
        return self.size

class paramnode:
    def __init__(self, idx, char):
        self.idx = idx
        self.size = 1
        self.char = char

    def evaluate(self, inp):
        return inp[self.idx]

    def display(self, indent=0):
        print ('%sp%d' % (' '*indent,self.idx))

    def getSize(self):
        return self.size

class constnode:
    def __init__(self, v, char):
        self.v = v
        self.size = 1
        self.char = char

    def evaluate(self, inp):
        return self.v

    def display(self, indent=0):
        print ('%s%d' % (' '*indent,self.v))

    def getSize(self):
        return self.size

addw = fwrapper(lambda l:l[0]+l[1],2,'add')
subw = fwrapper(lambda l:l[0]-l[1],2,'subtract')
mulw = fwrapper(lambda l:l[0]*l[1],2,'multiply')

def iffunc(l):
    if l[0]>0: return l[1]
    else: return l[2]
ifw = fwrapper(iffunc,3,'if')

def isgreater(l):
    if l[0]>l[1]: return 1
    else: return 0
gtw = fwrapper(isgreater,2,'isgreater')

flist = [addw, mulw, ifw, gtw, subw]


def makerandomtree(pc, maxdepth=4, fpr=0.5, ppr=0.6):
    if random()<fpr and maxdepth>0:
        f=choice(flist)
        children = [makerandomtree(pc, maxdepth-1, fpr, ppr)
                    for i in range(f.childcount)]
        return node(f, children, None)
    elif random()<ppr:
        return paramnode(randint(0,pc-1), None)
    else:
        return constnode(randint(0,10), None)


def makeTree(seed, maxDepth = 4):
    parsedSeed = seed.getParsableSeed()
    currChar =parsedSeed[:1]
    seed.setParsableSeed(parsedSeed[1:])

    _node = None

    if len(seed.getParsableSeed()) !=0:

        if (currChar in string.ascii_uppercase or currChar == seed.originalParsable[:1]) and maxDepth > 0:
            func = flist[getNormalizedVal(currChar)]
            
            children = []
            for i in range(func.childcount): 
                childNode = makeTree(seed, maxDepth-1)
                if childNode != None:
                    children.append(childNode)

            if len(children) != func.childcount:
                extra = func.childcount-len(children)
                for i in range(extra):
                    children.append(constnode(1, None))

#            children = [makeTree(seed, maxDepth-1) for i in range(func.childcount)]
            _node = node(func, children, currChar)

        elif currChar in string.ascii_lowercase:
            if int(string.ascii_lowercase.index(currChar)) % 2 ==0:
                _node = paramnode(0, currChar)

            else:
                _node = paramnode(1, currChar)

        else:
            if currChar in string.digits:
                _node = constnode(int(currChar), currChar)
            elif currChar in string.punctuation:
                _node = constnode(int(string.punctuation.index(currChar)/9), currChar)
            elif currChar in string.ascii_uppercase:
                _node = constnode(int(string.ascii_uppercase.index(currChar)), currChar)

    return _node


def getNormalizedVal(char):
    retVal = None

    if char in string.ascii_uppercase:
        retVal = int(string.ascii_uppercase.index(char)/4)
    elif char in string.ascii_lowercase:
        retVal = int(string.ascii_lowercase.index(char)/4)
    elif char in string.punctuation:
        retVal = int(string.punctuation.index(char)/4)
    else:
        retVal = int(int(char)/4)

    if retVal > 4:
        retVal = 4

    return retVal

def getSize(program):
    size = program.getSize()
    if size == 1:
        return False
    else:
        return size    


def mutate(t, pc, probchange=0.1):
    if random()<probchange:
        return makerandomtree(pc)
    else:
        result = deepcopy(t)
        if hasattr(t,"children"):
            result.children = [mutate(c,pc,probchange) for c in t.children]
        return result

def crossover(t1, t2, probswap=0.7, top=1):
    if random()<probswap and not top:
        return deepcopy(t2)
    else:
        result=deepcopy(t1)
        if hasattr(t1,'children') and hasattr(t2, 'children'):
            result.children=[crossover(c, choice(t2.children),probswap, 0)
                             for c in t1.children]
        return result

def scoreFunction(tree, s):    
    score =subprocess.check_output("./train.py")
    return score


def getrankfunction(dataset):
    def rankfunction(population):
        scores=[(scoreFunction(t,dataset),t) for t in population]
        scores.sort()
        return scores
    return rankfunction


def evolve(pc, popsize, rankfunction, maxgen=500, 
           mutationrate=0.1, breedingrate=0.4, pexp=0.7, pnew=0.05):
    def selectionIndex():
        return int(log(random()/log(pexp)))

    population = [makerandomree(pc) for i in range(popsize)]
    for i in range(maxgen):
        scores = rankfunction(population)
        print(scores[0][0])
        if scores[0][0]==0:
            break

        newpop=[scores[0][1],scores[1][1]]

        while len(newpop)<popsize:
            if random()>pnew:
                newpop.append(mutate(
                              crossover(scores[selectIndex()][1],
                                        scores[selectIndex()][1],
                                        probswap=breedingrate),
                                        pc, probchange = mutationrate))
            else:
                newpop.append(makerandomtree(pc))

        population=newpop
    scores[0][1].display()
    return scores[0][1]



#! /usr/bin/python

from random import random, randint, choice
from copy import deepcopy
from math import log

import json

class fwrapper:
    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name

class node:
    def __init__(self, fw, children):
        self.function = fw.function
        self.name = fw.name
        self.children = children
        self.size = 0

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
    def __init__(self, idx):
        self.idx = idx
        self.size = 1

    def evaluate(self, inp):
        return inp[self.idx]

    def display(self, indent=0):
        print '%sp%d' % (' '*indent,self.idx)

    def getSize(self):
        return self.size

class constnode:
    def __init__(self, v):
        self.v = v
        self.size = 1

    def evaluate(self, inp):
        return self.v

    def display(self, indent=0):
        print '%s%d' % (' '*indent,self.v)

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
        return node(f, children)
    elif random()<ppr:
        return paramnode(randint(0,pc-1))
    else:
        return constnode(randint(0,10))

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

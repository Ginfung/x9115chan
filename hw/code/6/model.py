import pdb, random, numpy
from o import *


def candidate(decs = [], scores =[], energy = None):
    return o(decs=decs, scores=scores, energy = energy)

r = random.random
def within(lo,hi): return lo + (hi - lo)*r()
def lt(x,t): return x < y # less than
def bt(x,y): return x > y # better than

class Has(object):
    def __init__(i,name='',lo=0,hi=1e32,init=0,
               goal=None,touch=True):
       i.name,i.lo,i.hi      = name,lo,hi
       i.init,i.goal,i.touch = init,goal,touch
       
    def restrain(i,x):
       if   x < i.lo: return i.lo
       elif x > i.hi: return i.hi
       else: return x
       
    def any(i):
       return within(i.lo,i.hi)
       
    def ok(i,x):
       return i.lo <= x <= i.hi
       
    def __repr__(i):
       return '%s=%s' % (i.name, o(name=i.name,lo=i.lo,hi=i.hi,init=i.init,goal=i.goal,touch=i.touch))
       

class model(object):
    def __init__(i, dec=[], obj=[]):
        i.dec = dec # should be Has list
        i.obj = obj # should be Has list
        i.decNum = len(i.dec)
        i.objNum = len(i.obj)

    def objectives(i):
        assert False, 'Should implement in the subclass'

    def learn_base_line(i, tries = 10000):
        for o in i.obj: o.lo, o.hi = 1e32, -1e32
        for _ in range(tries):
            while True:
                can = i.genCandidate(reEval=False)
                if can: break
            for f in range(i.objNum):
                t = i.objectives()[f](can)
                if t < i.obj[f].lo: i.obj[f].lo = t
                if t > i.obj[f].hi: i.obj[f].hi = t
        print '===== Base line study done! ===='
        

    def genCandidate(i, source = None, what = lambda x:x, reEval = True):
        if source is None:
            source = candidate(decs=[x.any() for x in i.dec]) # random genearted
        can = what(source)
        if i.ok(can):
            if reEval:
                can.scores = []
                can.energy = None 
                can = i.eval(can)
            return can
        else: return None

    def energy(i, scores):
        e = 0
        for o in range(i.objNum):
            e += (scores[o] - i.obj[o].lo) / (i.obj[o].hi-i.obj[o].lo)
        return e
        
    def eval(i, c):
        if not c.scores:
            c.scores = [obj(c) for obj in i.objectives()]
        if c.energy == None:
            c.energy = i.energy(c.scores)
        return c

    def ok(i, c):
        if c == None: return False
        for x in range(i.decNum):
            if not i.dec[x].ok(c.decs[x]): return False
        return True

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
    def __init__(i, decs=[], objs=[]):
        i.dec = decs # should be Has list
        i.obj = objs # should be Has list
        i.decNum = len(i.dec)
        i.objNum = len(i.obj)

    def objectives(i):
        assert False, 'Should implement in the subclass'

    def learn_base_line(i, tries = 1e4):
        for o in i.obj: o.lo, o.hi = 1e32, -1e32
        for _ in range(tries):
            while True:
                can = i.genCandidate()
                if can: break
            for f in range(i.objNum):
                t = i.objectives()[f](can)
                if t < i.obj[f].lo: i.obj[f].lo = t
                if t > i.obj[f].hi: i.obj[f].hi = t
        print '===== Base line study done! ===='
        

    def genCandidate(i, source = None, what = lambda x:x):
        if source is None:
            source = candidate(decs=[x.any() for x in i.dec]) # random genearted
        can = what(source)
        if i.ok(can): return can
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
        for x in range(i.decNum):
            if not i.dec[x].ok(c.decs[x]): return False
        return True

        
class Schaffer(model):
    def __init__(i):
        dec = [Has('x', -1e2, 1e2)]
        obj = [Has(name='f1', goal = lt, touch=False),
               Has(name='f2', goal = lt, touch=False)]
        model.__init__(i,dec,obj)
        
    def f1(i, c):
        x = c.decs[0]
        return x**2

    def f2(i,c):
        x = c.decs[0]
        return (x-2)**2

    def objectives(i):
        return [i.f1, i.f2]

class Osyczka2(model):
    def __init__(i):
        dec = [Has('x1', 0,10),
                Has('x2', 0,10),
                Has('x3', 1,5),
                Has('x4', 0,6),
                Has('x5', 1,5),
                Has('x6', 0,10)]
        obj = [Has(name='f1', goal = lt, touch=False),
               Has(name='f2', goal = lt, touch=False)]
        model.__init__(i,dec,obj)

    def f1(i,c):
        [x1,x2,x3,x4,x5,x6] = [x for x in c.decs]
        return -(25*(x1-2)**2+(x2-2)**2+(x3-1)**2*(x4-4)**2+(x5-1)**2)

    def f2(i,c):
        return sum(x**2 for x in c.decs)

    def ok(i,c):
        if not model.ok(i,c): return False
        [x1,x2,x3,x4,x5,x6] = [x for x in c.decs]
        g1 = x1+x2-2
        g2 = 6-x1-x2
        g3 = 2-x2+x1
        g4 = 2-x1+3*x2
        g5 = 4-(x3-3)**2-x4
	g6 = (x5-3)**3+x6-4
	return min(g1,g2,g3,g4,g5,g6) >= 0

    def objectives(i):
        return [i.f1,i.f2]
        
sss = Osyczka2()
sss.learn_base_line(1000)
pdb.set_trace()

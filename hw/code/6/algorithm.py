import math
import pdb
import sys
import numpy as np
from problem import *

say = lambda sign:sys.stdout.write(sign)

def sa(model):
    # basic simulated anneling parameters
    kmax = 3000
    emax = 1e-8
    
    def p(currE, nextE, t):
        return math.exp((currE-nextE)/t)
    
    print "Optimizer: simulated annealing"
    print "Model", model.__class__.__name__

    while True:
        c = model.genCandidate() # current
        if c: break
    c = model.eval(c)
    init = c
    best = init # best
    print 'k=0: ',
    for k in range(kmax):
        while True:
            n = model.genCandidate() # neighbor
            if n: break
        n = model.eval(n)
        if n.energy < best.energy: # best state found
            best = n
            say('!')
        if n.energy < c.energy:    # jump to better state
            c = n
            say('+')
        elif p(c.energy, n.energy, 1.0001 - float(k)/kmax) > r(): # jump to a worse state?
            c = n
            say('?')
        say('.')

        if k % 100 == 0 and k >0:
            print '\n'
            print 'k=%d:' % k,

    # final report
    print '\n'
    print '='*30
    print 'step k=', kmax
    print 'first trial: x=', init.decs
    print 'init energy:', init.energy
    print 'best solution: x=', best.decs
    print 'energy: ', best.energy
    print '~~~~~~end of report~~~~~~~~~~~~~~~\n\n\n\n'


def mws(model):
    # basic maxwalksat parameters
    kmax = 3000
    max_changes = 2
    p = 0.5
    step = 20

    print "Optimizer: max walk sat"
    print "Model", model.__class__.__name__

    def random_change_bit(source, bit):
        source.decs[bit] = random.uniform(model.dec[bit].lo,model.dec[bit].hi)
        if model.ok(source):
            source.scores = []
            source.energy = None
            source = model.eval(source)
            return source
        else: return None

    def study_one_bit(source, bit):
        bit_setting = np.linspace(model.dec[bit].lo, model.dec[bit].hi, step).tolist()
        best = source
        for i in bit_setting:
            source.decs[bit] = i
            if not model.ok(source): continue
            source.scores = []
            source.energy = None
            source = model.eval(source)
            if source.energy < best.energy:
                best = source
        return best

    # init sol
    while True:
        sol = model.genCandidate()
        if model.ok(sol): break
    init = sol
    best = sol
    old = sol

    print 'k=0: ',
    for k in range(kmax):
        while True:
            sol = model.genCandidate()
            if model.ok(sol): break
        for _ in range(max_changes):
            change = random.randint(0, model.decNum-1)
            if p < r():
                sol = random_change_bit(sol, change) or sol
            else:
                sol = study_one_bit(sol, change) or sol
        current = sol
        if current == None: continue
        if current.energy < best.energy: # new best solution found
            best = current
            say('!')
        if current.energy < old.energy: # better than the last generation
            say('+')
        else:
            say('.')
        
        old = current
        
        if k % 100 == 0 and k >0:
            print '\n'
            print 'k=%d:' % k,

    # final report
    print '\n'
    print '='*30
    print 'step k=', kmax
    print 'first trial: x=', init.decs
    print 'init energy:', init.energy
    print 'best solution: x=', best.decs
    print 'energy: ', best.energy
    print '~~~~~~end of report~~~~~~~~~~~~~~~\n\n\n\n'


"""
def main():
    m = (Kursawe())
    m.learn_base_line(10000)
    sa(m)
    mws(m)


if __name__ == '__main__':
    main()

"""

import pdb
from random import *
import numpy as np
import math
import sys

pdb.set_trace = lambda: None
x_l = int(-1e5)
x_u = int(1e5)
x = lambda:randrange(x_l,x_u)
seed(200065465) # set up the seed for random func


def schaffer(x):
    f1 = x**2
    f2 = (x-2)**2
    return float(f1+f2)


def find_baseline(f, trial):
    min = np.inf
    max = -np.inf
    for i in range(trial):
        t = schaffer(x())
        if t < min:
            min = t
        if t > max:
            max = t
    return [min,max]


def energy(xx, base_min, base_max):
    return (schaffer(xx) - base_min) / (base_max - base_min)


def neighbor(current, radius):
    #return randint(max(x_l, current-radius),min(x_u,current+radius))
    return randint(x_l,x_u)

def p(currE, nextE, t):
    return math.exp(-(nextE-currE)/t)

def sa(kmax = 1000, emax = 1e-8, neighborRadius = 1000):
    [base_min,base_max] = find_baseline(schaffer, int(1e6)) # find the baseline
    pdb.set_trace()
    s = x() # initial state
    init_s = s
    e = energy(s, base_min, base_max) # initial energy
    sb = s; eb = e
    k = 0
    pdb.set_trace()
    sign = str(k)+':'
    while k < kmax:
        sn = neighbor(s, neighborRadius)
        en = energy(sn, base_min, base_max)
        if en < eb: # best state found
            sb = sn
            eb = en
            sign += '!'
        if en < e: # jump to better state
            s = sn
            e = en
            sign += '+'
        elif p(e, en, 1.0001 - float(k)/kmax) > random(): # jump to a worse state?
            s = sn
            e = en
            sign += '?'
        sign += '.'
        k += 1
        if k % 50 == 0:
             print sign,
             print sb
             sign = str(k)+':'

    print '============'
    print 'step k = ',kmax
    print 'first trial: x = ',init_s
    print 'Best solution: x = ', sb
    print 'Objective schaffer = ', schaffer(sb)
            

def main():
    sa()



if __name__ == '__main__':
    main()

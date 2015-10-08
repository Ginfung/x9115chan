import pdb
import numpy as np
from random import *

lo = [0,0,0,1,0,1,0] # the 0th element is trival
hi = [0,10,10,5,6,5,10] # the 0th element is trival

def gen_rand_x(x_l, x_u):
    assert len(x_l) == len(x_u)
    return [uniform(x_l[i],x_u[i]) for i in range(len(x_l))]


def find_baseline(trial):
    min = np.inf
    max = -np.inf
    for i in range(trial):
        while True:
            x_t = gen_rand_x(lo,hi)
            if osyczka2_con(x_t):
                break
        t = osyczka2(x_t)
        if t < min:
            min = t
        if t > max:
            max = t
    return [min,max]


def energy(x, base_min, base_max):
    return (osyczka2(x) - base_min) / (base_max - base_min)


def osyczka2(x):
    f1 = -(25*(x[1]-2)**2+(x[2]-2)**2+(x[3]-1)**2*(x[4]-4)**2+(x[5]-1)**2)
    f2 = sum([i**2 for i in x[1:7]])
    return f1 + f2

def osyczka2_con(x):
    g1 = x[1] + x[2] -2
    g2 = 6 - x[1] - x[2]
    g3 = 2 - x[2] + x[1]
    g4 = 2 - x[1] + 3*x[2]
    g5 = 4 - (x[3]-3)**2 - x[4]
    g6 = (x[5]-3)**3 + x[6] -4
    return min(g1,g2,g3,g4,g5,g6) >= 0  # all gs should be ge 0

def random_change_bit(sol, bit, x_l, x_u):
    tol = 100 # avoid constraints too difficult to fulfill!
    copy = sol[:]
    while True:
        sol[bit] = uniform(x_l[bit], x_u[bit])
        if osyczka2_con(sol):
            return sol
        tol -= 1
        if tol < 0: return copy
        
def study_one_bit(sol, bit, x_l, x_u, step):
    global base_min, base_max
    bit_setting = np.linspace(x_l[bit], x_u[bit], step).tolist()
    be = energy(sol, base_min, base_max) # best energy
    bs = sol # best solution
    for i in bit_setting:
        sol[bit] = i
        if not osyczka2_con(sol): continue
        ce = energy(sol, base_min, base_max)
        if ce > be:
            be, bs = ce, sol
    return bs
    

def mws(max_trial = 1000, max_changes = 3, threshold = 0.99, p = 0.5, step = 20):
    global base_min, base_max
    for i in range(max_trial):
        while True:
            sol = gen_rand_x(lo, hi)
            if osyczka2_con(sol): break
        # initialze the first try as best solution, best energy
        if i == 0:
            bs = sol # best solution
            be = energy(sol, base_min, base_max) # best energy
            os, oe = bs, be
        # mutate the solution as maxwatsat
        for j in range(max_changes):
            if energy(sol, base_min, base_max) > threshold:
                print '\n', '='* 15
                print 'Threshold achieved!'
                print 'Solution:', sol
                print 'Energy:', energy(sol, base_min, base_max)
                return

            c = randint(1,6)
            if p < random():
                sol = random_change_bit(sol, c, lo, hi)
            else:
                sol = study_one_bit(sol, c, lo, hi, step)
        # update the record the mutated solution
        cs = sol
        ce = energy(cs, base_min, base_max)
        if ce > be: # new best solution found
            case = 1
            bs, be = cs, ce
        elif ce > oe: # better than the last generation
            case = 2
        else:
            case = 3  # worse than the last generation
        # printing the results
        if i % 40 == 0:
            print '\n',i, round(be,2), '|',
        if case == 1: print '!',
        if case == 2: print '+',
        if case == 3: print '.',
        os, oe = cs, ce
        
    # printing the final result
    print '\n', '='*15
    print 'Best solution:', [round(i,2) for i in bs[1:]]
    print 'Best energy:', be
            
def main():
    global base_max,base_min
    base_min, base_max = find_baseline(10**5) # find the baseline
    mws()


if __name__ == '__main__':
    main()

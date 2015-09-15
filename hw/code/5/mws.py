import pdb
import numpy as np
from random import *

x_l = [0,0,0,1,0,1,0]
x_u = [0,10,10,5,6,5,10]

def gen_rand_x(x_l,x_u):
    assert len(x_l) == len(x_u)
    return [uniform(x_l[i],x_u[i]) for i in range(len(x_l))]


def find_baseline(trial):
    min = np.inf
    max = -np.inf
    for i in range(trial):
        while True:
            x_t = gen_rand_x(x_l,x_u)
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
    return f1+ f2

def osyczka2_con(x):
    return x[1] + x[2] - 2 >= 0 and 6 - x[1] - x[2] >= 0 and 2 - x[2] + x[1] >= 0 and 2 - x[1]+3*x[2] >= 0 and 4 - (x[3]-3)**2 - x[4] >= 0 and (x[5]-3)**3 + x[6] -4 >=0


def mws(max_trial = 1000, max_chanes = 3, p = 0.5, steps = 10):
    print find_baseline(10**5)
    base_min = -370
    base_max = 145

    for i in range(max_trial):
        2


def main():
    mws()


if __name__ == '__main__':
    main()

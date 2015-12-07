from paretoRanking import *
import os,sys
parserdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/parser/'
sys.path.insert(0,parserdir)
from parser import *
import pdb,random



# Setting up the parameters for the corss-entropy
pop = 1000
rho = 0.1
gen = 30

def Bernoulli(p):
    if random.random() < p: return 1
    else: return 0

def genCandidate(P):
    d = [Bernoulli(i) for i in P]
    return candidate(decs=d, scores=[])

def CrossEntropy(model):
    print model
    n = len(model.dec)
    P = [0.5] * n
    w = 0
    for gen_c in range(gen):
        if w:
            S = [model.genRandomCan(True) for i in range(pop)]
            w = 0
        else:
            S = [genCandidate(P) for i in range(pop)]
        for i in S: model.ok(i)
        WORK = [i.decs+i.scores+[0] for i in S]
        #er = 0
        #for i in S:
         #   if model.ok(i):
          #      er += 1
        #print (er+0.0)/len(S)
        S_s = paretoRank(WORK, rho, n ,3)
        P = [sum(S_s[i][j] for i in range(len(S_s)))/float(len(S_s)) for j in range(n)]
        #print sorted(P)
        import numpy
        aa = numpy.median([i[n] for i in S_s])
        bb = numpy.median([i[n+1] for i in S_s])
        cc = numpy.median([i[n+2] for i in S_s])
        print '%f\t%f\t%f' % (aa,bb,cc)
    pdb.set_trace()
    return 1

def main(name):
    m = FTModel('../feature_tree_data/' + name + '.xml', name, '../ModelData/' + name + '.cost', 3)
    CrossEntropy(m)
    #pdb.set_trace()

if __name__ == '__main__':
    #main('eshop')
    #main('webportal')
    main('eis')

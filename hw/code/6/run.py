from algorithm import *

for model in [Schaffer, Osyczka2, Kursawe]:
    m = model()
    m.learn_base_line(10000)
    
    for optimizer in [sa, mws]:
        optimizer(m)


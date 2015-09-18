import pdb
from random import *

def had_duplicates(t):
    seen = set()
    for x in t:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False

def simulation():
    birthday = list()
    for i in range(23):
        birthday.append(randint(1,365))
    return had_duplicates(birthday)


n = 1000
c = 0
for i in range(n):
    if simulation():
        c += 1
chance = c/float(n)
print 'The chances that two of students has the same birthday is: ', chance 

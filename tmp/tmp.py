#!/usr/bin/python3

from itertools import *

################################################################################

def subsetsum(less=False, greater=False):
    def good(combination, tolerance):
        diff = sum(combination) - goal
        return -tolerance <= diff <= 0 if less else \
            tolerance >= diff >= 0 if greater else abs(diff) <= tolerance
    multiset = ([1000, 771, 880, 1300, 1300, 900, 1300, 1300, 400, 1300])
    goal = 5021
    tolerable = []
    tolerance = -1
    while not tolerable:
        tolerance += 1
        for combination in powerset(multiset):
            if good(combination, tolerance):
                tolerable.append(combination)
    mode = 'less' if less else 'greater' if greater else 'abs'
    print('mode: {}, tolerance: {}'.format(mode, tolerance))
    for combination in tolerable:
        print(sum(combination), combination)
    print()

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


################################################################################

def gram(vs):
    us = []
    for k in range(len(vs)):
        u = vs[k]
        for j in range(k - 1):
            u = add(u, mult(-1, proj(us[j], vs[k])))
        us.append(u)
    es = [unit(u) for u in us]
    print('us:', us)
    print('es:', es)

def proj(u, v):
    c = dot(u, v) / dot(u, u)
    return mult(c, u)

def unit(v):
    c = 1 / norm(v)
    return mult(c, v)

def mult(c, v):
    w = []
    for x in v:
        w.append(c * x)
    return w

def add(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(v1[i] + v2[i])
    return v

def norm(v):
    return sqrt(dot(v, v))

def dot(v1, v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i] * v2[i]
    return s

################################################################################

if __name__ == '__main__':
    subsetsum(less=True)
    subsetsum(greater=True)
    subsetsum()

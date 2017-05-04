#!/usr/bin/python3

from math import *
from sympy import *

############################################################
"""TUTOR"""

def tutor():
    # u1 = [2, -1, -1, 0]
    # u2 = [-1, 0, -2, 1]
    # v3 = [-0.5, 4, 1, 4.5]
    # u3 = add(v3, mul(-1, add(proj(u1, v3), proj(u2, v3))))
    # print(u3)
    v1 = [1, 0, 2, -1]
    v2 = [0, 1, -1, 1]
    vs = [v1, v2]
    es = gram(vs)
    print(es)

def gram(vs):
    n = len(vs)
    zero = []
    us = []
    for k in range(n):
        s = proj(us[0], vs[1])
        for j in range(k - 1):
            
        us.

    v1, v2 = vs
    u1 = v1
    u2 = add(v2, mul(-1, proj(u1, v2)))
    us = [u1, u2]
    es = [unit(u) for u in us]
    return es

def proj(u, v):
    c = dot(u, v) / dot(u, u)
    return mul(c, u)

def mul(c, v):
    v0 = []
    for e in v:
        v0.append(c * e)
    return v0

def add(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(v1[i] + v2[i])
    return v

def unit(v):
    c = 1 / norm(v)
    return mul(c, v)

def norm(v):
    return sqrt(dot(v, v))

def dot(v1, v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i] * v2[i]
    return s

############################################################
"""OS"""

def os():
    pass

def get_turnaround(times):
    previous = 0
    total = 0
    for time in times:
        total += previous + time
        previous += time
    return total / len(times)

############################################################

if __name__ == '__main__':
    pass
    tutor()
    # os()

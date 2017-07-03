#!/usr/bin/python3

from math import *
from sympy import *

############################################################
"""TUTOR"""

init_printing()

def tutor():
    var('u v')
    X = Matrix([-3*u / (u**2 + v**2), 9*v / (u**2 + v**2)])
    Y = Matrix([u, v])
    p = X.jacobian(Y).det()
    print(p)

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

############################################################

if __name__ == '__main__':
    pass
    tutor()

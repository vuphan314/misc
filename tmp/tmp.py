!/usr/bin/python3

from math import *
from sympy import *

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
"""TUTOR"""

def tutor():
    m = [1, 1, 1], [1, 1, 2], [2, 1, 1]
    m = Matrix(m)
    m = m.rref()
    print(m)

def A(x, y, z):
    return exp(-x**2 - y**2 / 4 - z**2 / 9)

def fx(x, y, z):
    return -400 * x * A(x, y, z)

def fy(x, y, z):
    return -100 * y * A(x, y, z)

def fz(x, y, z):
    return -400 / 9 * z * A(x, y, z)

def norm(v):
    a, b, c = v
    return sqrt(a**2 + b**2 + c**2)

def unit(v):
    n = norm(v)
    a, b, c = v
    return a / n, b / n, c / n

############################################################

if __name__ == '__main__':
    # os()
    tutor()

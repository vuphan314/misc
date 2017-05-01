#!/usr/bin/python3

from math import *
from sympy import *

############################################################
"""TUTOR"""

def tutor():
    P = Matrix([[-1, -3], [-3, -10]])
    Ap = Matrix([[4, 7], [2, 6]])
    A = P * Ap * P**-1
    print(A)

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

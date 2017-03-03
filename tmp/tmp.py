#!/usr/bin/python3

from math import *
# from sympy import *

############################################################

def get_turnaround(times):
    previous = 0
    total = 0
    for time in times:
        total += previous + time
        previous += time
    return total / len(times)

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
    # times = [2, 4, 1, 1, 1]
    # times = sorted(times)
    # turnaround = get_turnaround(times)
    # print(turnaround)
    p = 1, 1, -1
    v = fx(*p), fy(*p), fz(*p)
    n = norm(v)
    # print(v)
    # print(n)
    u = unit(v)
    print(u)

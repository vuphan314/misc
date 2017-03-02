#!/usr/bin/python3

from math import *
from sympy import *

############################################################

def get_turnaround(times):
    previous = 0
    total = 0
    for time in times:
        total += previous + time
        previous += time
    return total / len(times)

############################################################

if __name__ == '__main__':
    times = [2, 4, 1, 1, 1]
    times = sorted(times)
    turnaround = get_turnaround(times)
    print(turnaround)

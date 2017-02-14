#!/usr/bin/python3

from math import *
from sympy import *

############################################################

ram = 512 * 3
os = 100
proc = 200
n = (ram - os) // proc

p = 0.8

cpu = 1 - p ** n

############################################################

print(n, cpu)

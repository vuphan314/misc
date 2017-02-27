#!/usr/bin/python3

from math import *
from sympy import *

############################################################

var('x')

M = [
    [3 - 2*x**3 , -4 + 2*x**2 + 4*x**3, 0],
    [-x**3, 1 + x**2 + 2*x**3, 0],
    [-2 - 4*x**2, -4 + 8*x**2, 2 + 2*x**2]
]

M = Matrix(M)

d = M.det()
d = simplify(d)

i = M**-1
i = simplify(i)

############################################################

print(d)
print(i)

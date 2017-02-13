#!/usr/bin/python3

from sympy import *

m = [[4,-8,7],[-2,5,-5],[-1,2,-2]]
# e1i = [[1,0,0],[0,1,0],[3,0,1]]
m = Matrix(m)
# mi = m ** -1
p = m.det()
print(p)

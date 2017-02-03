from sympy import *

mat = [
    [2, 1, 4, 3, 15],
    [1, 0, 1, 1, 5],
    [0, 1, 1, 2, 6],
    [0, 1, 1, 2, 6],
    [2, -3, 1, 1, 4]
]

mat = Matrix(mat).rref()

p = mat
print(p)

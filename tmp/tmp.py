#!/usr/bin/python3

from fractions import *
from itertools import *

################################################################################

def subsetsum(less=False, greater=False):
    def good(combination, tolerance):
        diff = sum(combination) - goal
        return -tolerance <= diff <= 0 if less else \
            tolerance >= diff >= 0 if greater else abs(diff) <= tolerance
    multiset = [975, 975, 675, 975, 975, 975]
    goal = 4360
    tolerable = []
    tolerance = -1
    while not tolerable:
        tolerance += 1
        for combination in powerset(multiset):
            if good(combination, tolerance):
                tolerable.append(combination)
    mode = 'less' if less else 'greater' if greater else 'abs'
    print('mode: {}, tolerance: {}'.format(mode, tolerance))
    for combination in tolerable:
        print(sum(combination), combination)
    print()

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

################################################################################

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

################################################################################

def printPair(keyStr, value):
    FLOAT_FORMAT = '{:4.2f}'
    if type(value) == float:
        value = FLOAT_FORMAT.format(value)
    print(keyStr.ljust(10), value)

def getBinFloatStrFromDecFractionalPartStr(decFractionalPartStr='.1875', recursionDepth=20):
    fraction = Fraction(decFractionalPartStr)
    assert 0 < fraction < 1
    binDigits = []
    for _ in range(recursionDepth):
        fraction *= 2
        if fraction < 1:
            binDigits.append(0)
        elif fraction == 1:
            binDigits.append(1)
            break
        else:
            binDigits.append(1)
            fraction -= 1
    return ''.join([str(x) for x in binDigits])
def getBinFloatStrFromDecFloatStr(decFloatStr='+21.1875', recursionDepth=20): # +0b10101.0011
    sign = decFloatStr[0]
    decFloatStr = decFloatStr[1:]

    pointIndex = decFloatStr.index('.')

    integralPart = decFloatStr[:pointIndex]
    integralPart = bin(int(integralPart))

    fractionalPart = decFloatStr[pointIndex:]
    fractionalPart = getBinFloatStrFromDecFractionalPartStr(fractionalPart, recursionDepth)

    return sign + integralPart + '.' + fractionalPart

def getDecFloatFromBinFractionalPartStr(mantissa='01111110100000000000000'):
    decFloat = 1 # 1.{mantissa}
    for i in range(len(mantissa)):
        if mantissa[i] == '1':
            decFloat += 2 ** -(i+1)
    return decFloat

def getDecIeeeFloatFromBinIeeeStr(binIeeeStr='11000100101111110100000000000000'):
    sign = binIeeeStr[0]
    exponent = binIeeeStr[1:9]
    mantissa = binIeeeStr[9:]

    signFactor = (-1) ** (sign == '1')
    exponentFactor = 2**(int(exponent, base=2) - 127)
    mantissaFactor = getDecFloatFromBinFractionalPartStr(mantissa)

    return signFactor * exponentFactor * mantissaFactor

def question05():
    MEM = 5
    DEC = 1
    ALU = 2
    REG = .25

    def pipeline0():
        cycle = 2 * (MEM + REG) + DEC + ALU
        print(cycle)

    def pipeline3():
        fetch = MEM
        decode = DEC
        execute = 2 * REG + MEM + ALU
        cycle = max(fetch, decode, execute)
        printPair('fetch', fetch)
        printPair('decode', decode)
        printPair('execute', execute)
        printPair('cycle', cycle)

    def pipeline5():
        fetch = MEM
        decode = DEC + REG
        execute = ALU
        access = MEM
        write = REG
        cycle = max(fetch, decode, execute, access, write)
        printPair('fetch', fetch)
        printPair('decode', decode)
        printPair('execute', execute)
        printPair('access', access)
        printPair('write', write)
        printPair('cycle', cycle)

    # pipeline0()
    # pipeline3()
    pipeline5()

def question06():
    def printHexNum():
        hexNum = bin(0x136A60)[2:]

        sign = hexNum[0]
        exponent = hexNum[1:8]
        mantissa = hexNum[8:]

        printPair('sign', sign)
        printPair('exponent', exponent)
        printPair('mantissa', mantissa)


    def printDecNum():
        decNum = '-21.1875'
        decNum = getBinFloatStrFromDecFloatStr(decNum)
        print(decNum)

    printHexNum()
    printDecNum()

def question13():
    def printColumn(nums):
        print('\n'.join(['\t{}'.format(num) for num in nums]))

    def printDiffs(nums, printing=True):
        diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
        if printing:
            printColumn(diffs)
        return diffs

    fxs = [x**4 for x in range(1, 8)]
    print('f(x)')
    printColumn(fxs)

    print('1st diffs')
    diffs1 = printDiffs(fxs)

    print('2nd diffs')
    diffs2 = printDiffs(diffs1)

    print('3rd diffs')
    diffs3 = printDiffs(diffs2)

    print('4th diffs')
    diffs4 = printDiffs(diffs3)

def question14():
    print(getDecIeeeFloatFromBinIeeeStr())

################################################################################

if __name__ == '__main__':
    # question05()
    # question06()
    # question13()
    question14()

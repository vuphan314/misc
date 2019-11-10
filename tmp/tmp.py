#!/usr/bin/python3

from fractions import *
from itertools import *

################################################################################

def powerset(iterable): # [1,2,3] |-> [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

################################################################################
'''COMP 554 midterm'''

def printPair(keyStr, value):
    FLOAT_FORMAT = '{:.10f}'
    if type(value) == float:
        value = FLOAT_FORMAT.format(value)
    print('\t', keyStr.ljust(15), value)

def getBase2DecStrFromBase10FractionalPartDecStr(base10FractionalPartDecStr, recursionDepth): # '.5' |-> '.1'
    assert base10FractionalPartDecStr[0] == '.'
    fraction = Fraction(base10FractionalPartDecStr)
    bits = []
    for _ in range(recursionDepth):
        fraction *= 2
        if fraction < 1:
            bits.append(0)
        elif fraction == 1:
            bits.append(1)
            break
        else: # fraction > 1
            bits.append(1)
            fraction -= 1
    return ''.join([str(bit) for bit in bits])
def getBase2DecStrFromBase10DecStr(base10DecStr, recursionDepth=20): # '+1.5 |-> '1.1'
    sign = base10DecStr[0]
    assert sign in {'+', '-'}

    base10DecStr = base10DecStr[1:]
    decPointIndex = base10DecStr.index('.')

    base10IntegralPartDecStr = base10DecStr[:decPointIndex]
    base2IntegralPartDecStr = bin(int(base10IntegralPartDecStr))

    base10FractionalPartDecStr = base10DecStr[decPointIndex:]
    base2FractionalPartDecStr = getBase2DecStrFromBase10FractionalPartDecStr(base10FractionalPartDecStr, recursionDepth)

    return sign + base2IntegralPartDecStr + '.' + base2FractionalPartDecStr

def getBase10FloatFromBase2FractionalPartDecStr(base2FractionalPartDecStr): # '.1' |-> .5
    base10Float = 0
    for i in range(len(base2FractionalPartDecStr)):
        if base2FractionalPartDecStr[i] == '1': # effectively skips leading '.'
            base10Float += 2 ** -i
    return base10Float
def getBase10FloatFromBase2DecStr(base2DecStr): # '+1.1' |-> 1.5
    assert base2DecStr[0] in {'+', '-'}

    sign = (-1) ** (base2DecStr[0] == '-')
    base2DecStr = base2DecStr[1:]

    decPointIndex = base2DecStr.index('.')

    base2IntegralPartDecStr = base2DecStr[:decPointIndex]
    base10IntegralPartDecStr = int(base2IntegralPartDecStr, base=2)

    base2FractionalPartDecStr = base2DecStr[decPointIndex:]
    base10FractionalPartDecStr = getBase10FloatFromBase2FractionalPartDecStr(base2FractionalPartDecStr)

    return sign * (base10IntegralPartDecStr + base10FractionalPartDecStr)

def getBase10FloatFromBase2MantissaStr(mantissa): # '10000000000000000000000' |-> .5
    return 1 + getBase10FloatFromBase2FractionalPartDecStr('.' + mantissa)
def getBase10FloatFromBase2IeeeStr(base2IeeeStr): # '00111111110000000000000000000000' |-> 1.5
    sign = base2IeeeStr[0]
    exponent = base2IeeeStr[1:9]
    mantissa = base2IeeeStr[9:]

    signFactor = (-1) ** (sign == '1')
    exponentFactor = 2**(int(exponent, base=2) - 127)
    mantissaFactor = getBase10FloatFromBase2MantissaStr(mantissa)

    return signFactor * exponentFactor * mantissaFactor

def question05():
    MEM = 5
    DEC = 1
    ALU = 2
    REG = .25

    def pipeline0():
        cycle = 2 * (MEM + REG) + DEC + ALU
        printPair('cycle', cycle)

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

    print('pipeline0')
    pipeline0()

    print('pipeline3')
    pipeline3()

    print('pipeline5')
    pipeline5()

def question06():
    def analyzeBase16Num():
        num = bin(0x136A60)[2:] # strips leading '0b'

        sign = num[0]
        exponent = num[1:8]
        mantissa = num[8:]

        printPair('sign', sign)
        printPair('exponent', exponent)
        printPair('mantissa', mantissa)

    def analyzeBase10Num():
        num = getBase2DecStrFromBase10DecStr('-21.1875')
        print(num)

    print('analyzeBase16Num')
    analyzeBase16Num()

    print('analyzeBase10Num')
    analyzeBase10Num()

def question13():
    def printColumn(nums):
        print('\n'.join(['\t{}'.format(num) for num in nums]))

    def printDiffs(nums, printing=True):
        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
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
    print(getBase10FloatFromBase2IeeeStr('11000100101111110100000000000000'))

def question15():
    num = bin(0xC5AB934D)[2:]
    print(getBase10FloatFromBase2IeeeStr(num))

def question16():
    def row2():
        print('row2')
        base10DecStr = '+' + str(3 / 8)
        base2DecStr = getBase2DecStrFromBase10DecStr(base10DecStr)
        printPair('base2DecStr', base2DecStr)
        printPair('base10DecStr', base10DecStr)
    def row3():
        print('row3')
        base2DecStr = '+10.1101'
        base10Float = getBase10FloatFromBase2DecStr(base2DecStr)
        base10Fraction = Fraction(base10Float)
        printPair('base10Fraction', base10Fraction)
        printPair('base10Float', base10Float)
    def row4():
        print('row4')
        base10DecStr = '+5.625'
        base2DecStr = getBase2DecStrFromBase10DecStr(base10DecStr)
        base10Fraction = Fraction(base10DecStr)
        printPair('base10Fraction', base10Fraction)
        printPair('base2DecStr', base2DecStr)

    row2()
    row3()
    row4()

def question22():
    num = getBase10FloatFromBase2IeeeStr('00111101110011001100110011001101')
    print(num)

def midterm():
    # question05()
    # question06()
    # question13()
    # question14()
    # question15()
    # question16()
    question22()

################################################################################

if __name__ == '__main__':
    midterm()

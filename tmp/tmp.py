#!/usr/bin/python3

from fractions import *
from itertools import *
from math import *

################################################################################

KiB = 2**10
MiB = 2**20
GiB = 2**30

def lg2(x):
    return log(x, 2)

def powerset(iterable): # [1,2,3] |-> [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def addSeparators(string, separator=' ', spacing=4):
    return separator.join(string[i : i + spacing] for i in range(0, len(string), spacing))

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
            base10Float += 2**-i
    return base10Float
def getBase10FloatFromBase2DecStr(base2DecStr): # '+1.1' |-> 1.5
    assert base2DecStr[0] in {'+', '-'}

    sign = (-1)**(base2DecStr[0] == '-')
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

    signFactor = (-1)**(sign == '1')
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
'''COMP 554 final'''

def getTime(hitRate, hitTime, missTime):
    return hitRate * hitTime + (1 - hitRate) * missTime

def answer_02():
    hitTime = 1
    missTime = 10
    for hitRate in [.97, .99]:
        time = getTime(hitRate, hitTime, missTime)
        print(time)

def answer_03():
    hitTime = 1
    missTime = 50
    for hitRate in [.97, .99]:
        time = getTime(hitRate, hitTime, missTime)
        print(time)

def answer_04_p1():
    mainSize = 128 * KiB
    cacheSize = 16 * KiB
    blockSize = 256

    sets = cacheSize / blockSize
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = lg2(mainSize)

    tagBits = mainBits - blockBits - setBits
    print(tagBits)

def answer_04_p2():
    mainSize = 32 * GiB
    cacheSize = 32 * KiB
    blockSize = KiB

    sets = cacheSize / blockSize
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = lg2(mainSize)

    tagBits = mainBits - blockBits - setBits
    print(tagBits)

def answer_04_p3():
    cacheSize = 512 * KiB
    blockSize = KiB
    tagBits = 7

    sets = cacheSize / blockSize
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = tagBits + setBits + blockBits
    mainSize = 2**mainBits
    mainSize /= MiB
    print(mainSize, 'MiB')

def answer_04_p4():
    mainSize = 16 * GiB
    blockSize = 4 * KiB
    tagBits = 10

    mainBits = lg2(mainSize)

    blockBits = lg2(blockSize)

    setBits = mainBits - tagBits - blockBits
    sets = 2**setBits

    cacheSize = sets * blockSize
    cacheSize /= MiB
    print(cacheSize, 'MiB')

def answer_04_p5():
    mainSize = 64 * MiB
    tagBits = 10

    mainBits = lg2(mainSize)

    setAndBlockBits = mainBits - tagBits

    cacheSize = 2**setAndBlockBits
    cacheSize /= KiB
    print(cacheSize, 'KiB')

def answer_04_p6():
    cacheSize = 512 * KiB
    tagBits = 7

    setAndBlockBits = lg2(cacheSize)

    mainBits = tagBits + setAndBlockBits

    mainSize = 2**mainBits
    mainSize /= MiB
    print(mainSize, 'MiB')

def getSets(cacheSize, blockSize, blocksPerSet):
    return cacheSize / blockSize / blocksPerSet

def getTagBits(mainBits, sets, blockSize):
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    tagBits = mainBits - setBits - blockBits
    return tagBits

def getTotalTagBits(cacheSize, blockSize, tagBits):
    blocks = cacheSize / blockSize

    totalTagBits = blocks * tagBits
    return totalTagBits

def answer_06():
    mainBits = 42

    cacheSize1 = 128 * KiB
    blockSize1 = 64
    blocksPerSet1 = 1

    cacheSize2 = MiB
    blockSize2 = 512
    blocksPerSet2 = 8

    sets1 = getSets(cacheSize1, blockSize1, blocksPerSet1)
    sets2 = getSets(cacheSize2, blockSize2, blocksPerSet2)

    tagBits1 = getTagBits(mainBits, sets1, blockSize1)
    tagBits2 = getTagBits(mainBits, sets2, blockSize2)

    def answer1():
        print(sets1)
        print(sets2)

    def answer2():
        print(tagBits1)
        print(tagBits2)

    def answer3():
        totalTagBits1 = getTotalTagBits(cacheSize1, blockSize1, tagBits1)
        totalTagBits2 = getTotalTagBits(cacheSize2, blockSize2, tagBits2)

        print(totalTagBits1)
        print(totalTagBits2)

    # answer1()
    # answer2()
    answer3()

def getCyclesPerInstruction(instructions, exeTime, cycleTime):
    instructionTime = exeTime / instructions
    cyclesPerInstruction = instructionTime / cycleTime
    return cyclesPerInstruction

def getSpeedup(cycleTime, instructionsNew, cyclesPerInstructionNew, exeTimeOld):
    exeTimeNew = cyclesPerInstructionNew * instructionsNew * cycleTime
    speedup = exeTimeOld / exeTimeNew
    return speedup

def answers_10_14(): # Note: give answers to three decimal places, for example: 88.123.
    cycleTime = 1e-9

    instructionsA = 1e9
    exeTimeA = 1.1

    instructionsB = 1.2e9
    exeTimeB = 1.5

    cyclesPerInstructionA = getCyclesPerInstruction(instructionsA, exeTimeA, cycleTime)
    cyclesPerInstructionB = getCyclesPerInstruction(instructionsB, exeTimeB, cycleTime)

    instructionsNew = 6e8
    cyclesPerInstructionNew = 1.1

    def answer10():
        print(cyclesPerInstructionA)

    def answer11():
        print(cyclesPerInstructionB)

    def answer12():
        clockRateAOverClockRateB = cyclesPerInstructionB * instructionsB / cyclesPerInstructionA / instructionsA
        print(clockRateAOverClockRateB)

    def answer13():
        speedupA = getSpeedup(cycleTime, instructionsNew, cyclesPerInstructionNew, exeTimeA)
        print(speedupA)

    def answer14():
        speedupB = getSpeedup(cycleTime, instructionsNew, cyclesPerInstructionNew, exeTimeB)
        print(speedupB)

    # answer10()
    # answer11()
    # answer12()
    # answer13()
    answer14()

def answer_15():
    opcode = bin(0x33)[2:].rjust(7, '0')
    funct3 = bin(0x0)[2:].rjust(3, '0')
    funct7 = bin(0x20)[2:].rjust(7, '0')
    rs2 = bin(5)[2:].rjust(5, '0')
    rs1 = bin(7)[2:].rjust(5, '0')
    rd = bin(6)[2:].rjust(5, '0')

    instruction = funct7 + rs2 + rs1 + funct3 + rd + opcode
    instruction = addSeparators(instruction)
    print(instruction)

def answer_17():
    base2DecStr = getBase2DecStrFromBase10DecStr('+63.25')
    # print(base2DecStr) # 111111.01 == 1.1111101 * 2**5

    signBit = '0'

    bias = 127
    exponentBits = bin(bias + 5)[2:].rjust(8, '0')

    fractionBits = '1111101'.ljust(23, '0')

    ieeeBits = signBit + exponentBits + fractionBits
    ieeeBits = addSeparators(ieeeBits)
    print(ieeeBits) # 0100 0010 0111 1101 0000 0000 0000 0000

def answer_25_p1():
    mainSize = 128 * KiB
    cacheSize = 16 * KiB
    blockSize = 256
    blocksPerSet = 2

    blocks = cacheSize / blockSize
    sets = blocks / blocksPerSet
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = lg2(mainSize)

    tagBits = mainBits - setBits - blockBits
    print(tagBits)

def answer_25_p2():
    mainSize = 32 * GiB
    cacheSize = 32 * KiB
    blockSize = KiB
    blocksPerSet = 4

    blocks = cacheSize / blockSize
    sets = blocks / blocksPerSet
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = lg2(mainSize)

    tagBits = mainBits - setBits - blockBits
    print(tagBits)

def answer_25_p3():
    cacheSize = 512 * KiB
    blockSize = KiB
    tagBits = 7
    blocksPerSet = 8

    blocks = cacheSize / blockSize
    sets = blocks / blocksPerSet
    setBits = lg2(sets)

    blockBits = lg2(blockSize)

    mainBits = tagBits + setBits + blockBits

    mainSize = 2**mainBits
    mainSize /= MiB
    print(mainSize, 'MiB')

def answer_25_p4():
    mainSize = 16 * GiB
    # blockSize = 4 * KiB
    tagBits = 10
    blocksPerSet = 4

    mainBits = lg2(mainSize)

    setAndBlockBits = mainBits - tagBits

    cacheSizePerWay = 2**setAndBlockBits

    cacheSize = cacheSizePerWay * blocksPerSet
    cacheSize /= MiB
    print(cacheSize, 'MiB')

def answer_25_p5():
    mainSize = 64 * MiB
    tagBits = 10
    blocksPerSet = 4

    mainBits = lg2(mainSize)

    setAndBlockBits = mainBits - tagBits

    cacheSizePerWay = 2**setAndBlockBits

    cacheSize = cacheSizePerWay * blocksPerSet
    cacheSize /= KiB
    print(cacheSize, 'KiB')

def answer_25_p6():
    cacheSize = 512 * KiB
    tagBits = 7
    blocksPerSet = 8

    cacheSizePerWay = cacheSize / blocksPerSet
    setAndBlockBits = lg2(cacheSizePerWay)

    mainBits = tagBits + setAndBlockBits

    mainSize = 2**mainBits
    mainSize /= MiB
    print(mainSize, 'MiB')

def getDieArea(diameter, dies):
    waferArea = pi * diameter**2 / 4
    dieArea = waferArea / dies
    return dieArea

def getWaferYield(diameter, dies, defectRate):
    dieArea = getDieArea(diameter, dies)
    waferYield = (1 + defectRate * dieArea / 2)**-2
    return waferYield

def getDieCost(waferCost, dies, waferYield):
    dieCost = waferCost / dies / waferYield
    return dieCost

def getDefectRate(waferYield): # cm^-2
    dieArea = 200 # mm^2
    dieArea /= 100 # cm^2
    defectRate = 2 * (waferYield**-.5 - 1) / dieArea
    return defectRate

def answers_28_37(): # Note: give answers to four decimal places, for example: 99.1234.
    diameter15 = 15 # cm
    waferCost15 = 12
    dies15 = 84
    defectRate15 = .02 # cm^-2

    diameter20 = 20 # cm
    waferCost20 = 15
    dies20 = 100
    defectRate20 = .031 # cm^-2

    waferYield15 = getWaferYield(diameter15, dies15, defectRate15)
    waferYield20 = getWaferYield(diameter20, dies20, defectRate20)

    dies15New = dies15 * 1.1
    dies20New = dies20 * 1.1

    defectRate15New = defectRate15 * 1.15
    defectRate20New = defectRate20 * 1.15

    def answer28():
        print(waferYield15)

    def answer29():
        print(waferYield20)

    def answer30():
        dieCost15 = getDieCost(waferCost15, dies15, waferYield15)
        print(dieCost15)

    def answer31():
        dieCost20 = getDieCost(waferCost20, dies20, waferYield20)
        print(dieCost20)

    def answer32():
        dieArea15New = getDieArea(diameter15, dies15New)
        print(dieArea15New)

    def answer33():
        dieArea20New = getDieArea(diameter20, dies20New)
        print(dieArea20New)

    def answer34():
        waferYield15New = getWaferYield(diameter15, dies15New, defectRate15New)
        print(waferYield15New)

    def answer35():
        waferYield20New = getWaferYield(diameter20, dies20New, defectRate20New)
        print(waferYield20New)

    def answer36():
        defectRate92 = getDefectRate(.92)
        print(defectRate92)

    def answer37():
        defectRate95 = getDefectRate(.95)
        print(defectRate95)

    # answer28()
    # answer29()
    # answer30()
    # answer31()
    # answer32()
    # answer33()
    # answer34()
    # answer35()
    # answer36()
    answer37()

def final():
    # answer_02()
    # answer_03()
    # answer_04_p1()
    # answer_04_p2()
    # answer_04_p3()
    # answer_04_p4()
    # answer_04_p5()
    # answer_04_p6()
    # answer_06()
    # answers_10_14()
    # answer_15()
    # answer_17()
    # answer_25_p1()
    # answer_25_p2()
    # answer_25_p3()
    # answer_25_p4()
    # answer_25_p5()
    # answer_25_p6()
    answers_28_37()

################################################################################
'''projected model counting'''

def counterexample():
    B = [0, 1]
    for f00 in B:
        for f01 in B:
            for f10 in B:
                for f11 in B:
                    pmc = max(f00, f01) + max(f10, f11)
                    mmap = max(f00 + f10, f01 + f11)
                    if pmc != mmap:
                        print(
                            'f00={}'.format(f00),
                            'f01={}'.format(f01),
                            'f10={}'.format(f10),
                            'f11={}'.format(f11),
                            'pmc={}'.format(pmc),
                            'mmap={}'.format(mmap),
                        )

################################################################################

if __name__ == '__main__':
    pass
    counterexample()

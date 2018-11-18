#!/usr/bin/python3

'''quiz 9'''

def printReturn(text, num, v=False):
    if v:
        print(text.ljust(20), str(num).rjust(10))
    return num

def q1(v=False): # EU(a1)
    return printReturn('q1 = EU(a1)', .25 * 2000 + .75 * 8000, v)

def q2(v=False): # EU(a0)
    return printReturn('q2 = EU(a0)', .25 * 10000 + .75 * 0, v)

def q3(v=False): # EU(A)
    return printReturn('q3 = EU(A)', max(q1(), q2()), v)

def q4(v=False): # EU(a1 | i1)
    return printReturn('q4 = EU(a1 | i1)', .7 * 2000 + .3 * 8000, v)

def q5(v=False): # EU(a0 | i1)
    return printReturn('q5 = EU(a0 | i1)', .7 * 10000 + .3 * 0, v)

def q6(v=False): # EU(a1 | i0)
    return printReturn('q6 = EU(a1 | i0)', .1 * 2000 + .9 * 8000, v)

def q7(v=False): # EU(a0 | i0)
    return printReturn('q7 = EU(a0 | i0)', .1 * 10000 + .9 * 0, v)

def q8(v=False): # EU(A_i1 | i1)
    return printReturn('q8 = EU(A_i1 | i1)', max(q4(), q5()), v)

def q9(v=False): # EU(A_i0 | i0)
    return printReturn('q9 = EU(A_i0 | i0)', max(q6(), q7()), v)

def q10(v=False): # EU(A_I | I)
    return printReturn('q10 = EU(A_I | I)', .25 * q8() + .75 * q9(), v)

def q11(v=False): # VPI(I)
    return printReturn('q11 = VPI(I)', q10() - q3(), v)

def main():
    q1(True)
    q2(True)
    q3(True)
    q4(True)
    q5(True)
    q6(True)
    q7(True)
    q8(True)
    q9(True)
    q10(True)
    q11(True)

if __name__ == '__main__':
    main()

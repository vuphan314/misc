# COMP 511: Written Assignment 3
Vu Phan, `vhp1`

## Topic
continuation-passing-style (CPS) transformations

## Exemplifying PL feature or idiom
Python's idioms for transforming from direct style to CPS

## Description of features and limitations

### Features

In Python, a function often returns a value (direct style).
```py
def successor(x): return x + 1
```
In this case, it is implicit where the value `x + 1` will be returned to.

To make it explicit, we can make the function `successor` continue with the value `x + 1` by passing it as an argument to a *continuation*.
The idiomatic way to do that is:
```py
def successor(x, c): # CPS, where `c` is the continuation (a unary function)
  c(x + 1)
```
In some sense, continuations are *`goto`s with arguments*.

CPS transformations apply to not only user-defined functions but also built-in operations.
For example:
```py
def plus(x, y, c): c(x + y)
```

In CPS, we turn function applications inside out.
That is, a more outer function application corresponds to a more deeply nested continuation.
For instance, consider the following complete program.
```py
def successor(x, c): c(x + 1)

def plus(x, y, c): c(x + y)

def plus_successor(x, y, c): # does (x + 1) + y
  successor(x, lambda v, y=y, c=c: plus(v, y, c))
```

### Limitations

Although CPS' explicit control flows enable us to manipulate execution much more freely, they also have disadvantages.
0. First, CPS code is harder to read than direct style code, which is more familiar to most programmers.
As shown in the complete Python program above, CPS code distracts readers with technical mechanisms of control flow reification (all the continuations being explicitly passed as arguments).
0. Second, similar to their `goto` analogy, continuations are potential traps for buggy spaghetti code. A programmer may accidentally mutate a continuation, creating a subtle bug that is hard to track down.

## Reference

[https://www.ps.uni-saarland.de/~duchier/python/continuations.html](https://www.ps.uni-saarland.de/~duchier/python/continuations.html)
[https://softwareengineering.stackexchange.com/a/278798](https://softwareengineering.stackexchange.com/a/278798)

#!/bin/env python3
from term import Term, add, mul
from sympy import sin
from fit import to_lambda

#x * sin(x) + x

tree = Term(add, Term(mul, Term(), Term(sin, Term())), Term())

print("Raw term tree: " + str(tree))
print("Expression: " + str(tree.collapse()))

f = to_lambda(tree.collapse(), 0)
print("evaluated at 5: " + str(f(5)))

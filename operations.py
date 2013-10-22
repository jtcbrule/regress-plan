'''
operations.py
Stores operations to be used in expression trees
'''

from __future__ import division

import sympy
import random

x = sympy.symbols('x')

def to_lambda(expr, constants):
    """ Convert sympy expression of x and constants to python lambda function.
        Note that all expressions are assumed to be functions of at least x,
        so the constants list should not contain Symbol('x').

        expr - sympy symbolic expression composed of x and c1, ..., ck
        constants - list of constants (e.g. [c1, c2])
    """
    return sympy.lambdify([x] + constants, expr)

''' Unary: '''
sqrt = sympy.sqrt
log = sympy.log
sin = sympy.sin
tan = sympy.tan

unary_ops = [sqrt, log, sin, tan]

''' Binary: '''
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

add.__name__ = '+'
sub.__name__ = '-'
mul.__name__ = '*'
div.__name__ = '/'

binary_ops = [add, sub, mul, div]

def get_random_unary_op():
    return random.choice(unary_ops)

def get_random_binary_op():
    return random.choice(binary_ops)
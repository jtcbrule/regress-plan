'''
operations.py
Stores operations/utility functions to be used in expression trees
'''

from __future__ import division

import sympy
import random

MAX_CONSTANTS = 10

''' c[k] = Symbol('ck'); note that c[0] = Symbol('x') '''
x = sympy.symbols('x')
c = list(sympy.symbols('c1:' + str(MAX_CONSTANTS)))
c.insert(0, x)

def to_lambda(expr, num_param):
    """ Return a (python) lambda expression 

        expr - symbolic expression composed of x and c1, ..., ck
        num_param - number of parameters (e.g. f(x; c1, c2) has 2 params)
        
        Note that expr cannot contain constant ck for k > num_param
    """
    return sympy.lambdify(c[0:(num_param + 1)], expr)

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

''' Constant: '''
''' These are special because they need a second parameter c, the name of the constant '''
add_constant = lambda c : lambda x : x + c
add_constant.__name__ = "add_c"
mult_by_constant = lambda c : lambda x : x * c
mult_by_constant.__name__ = "mult_c"

def get_random_unary_op():
    return random.choice(unary_ops)

def get_random_binary_op():
    return random.choice(binary_ops)
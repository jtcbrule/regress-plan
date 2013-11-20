'''
operations.py
Operations to be used in expression trees
'''

import sympy
import random

x = sympy.symbols('x')

''' Unary: '''
sqrt = sympy.sqrt
log = sympy.log
sin = sympy.sin
cos = sympy.cos
tan = sympy.tan
exp = sympy.exp
atan = sympy.atan

def unary_minus(x):
    return -1 * x

unary_minus.__name__ = '-'

unary_ops = [sqrt, log, sin, tan, exp, atan, unary_minus]

''' Binary: '''
def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

add.__name__ = '+'
mul.__name__ = '*'
div.__name__ = '/'

binary_ops = [add, mul, div]

def get_random_unary_op():
    return random.choice(unary_ops)

def get_random_binary_op():
    return random.choice(binary_ops)

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
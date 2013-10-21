'''
operations.py
Stores operations to be used in expression trees
'''

import sympy
import random

''' Unary: '''

sqrt = sympy.sqrt
log = sympy.log
sin = sympy.sin
tan = sympy.tan

unary_ops = [sqrt, log, sin, tan]

''' Binary: '''

add = lambda x1, x2 : x1 + x2
subtract = lambda x1, x2 : x1 - x2
multiply = lambda x1, x2 : x1 * x2
divide = lambda x1, x2 : x1 / x2 if x2 != 0 else float("inf")

binary_ops = [add, subtract, multiply, divide]


''' Constant: '''
''' These are special because they need a second parameter c, the name of the constant '''
add_constant = lambda c : lambda x : x + c
add_constant.__name__ = "Add constant"
mult_by_constant = lambda c : lambda x : x * c
mult_by_constant.__name__ = "Mult constant"



def get_random_unary_op():
    return random.choice(unary_ops)

def get_random_binary_op():
    return random.choice(binary_ops)
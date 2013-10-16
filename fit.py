#!/bin/env python3
from sympy import symbols, Lambda
from scipy.optimize import curve_fit

# maximum number of constants in a symbolic expression
MAX_CONSTANTS = 10

# all functions are single-var functions of x
x = symbols('x')

# constants (note that c[0] = x)
c = list(symbols('c1:' + str(MAX_CONSTANTS)))
c.insert(0, x)

def to_function(expr, num_param):
    """ Return a (python) lambda expression 

        expr - symbolic expression composed of x and c1...ck
        num_param - number of parameters (e.g. f(x; c1, c2) has 2 params)
        
        Note that expr cannot contain constant ck for k > num_param
    """
    return Lambda(c[:(num_param + 1)], expr)


sample_expr = c[2] * x**2 + c[1]

f = to_function(sample_expr, 2)

print(f(1,1,1))



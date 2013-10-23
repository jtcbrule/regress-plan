'''
fit.py
Utility functions for curve fitting sympy expressions
'''

import sympy
from scipy.optimize import curve_fit
import numpy as np

def to_lambda(expr, constants):
    """ Convert sympy expression composed of x and constants to python lambda.
        Note that all expressions are assumed to be functions of at least x,
        so the constants list should not contain Symbol('x').

        expr - sympy symbolic expression composed of x and c1, ..., ck
        constants - list of constants (e.g. [c1, c2])
    """
    return sympy.lambdify([sympy.symbols('x')] + constants, expr)

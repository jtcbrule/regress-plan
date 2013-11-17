'''
fit.py
Utility functions for curve fitting sympy expressions
'''

import sympy
import scipy.optimize
import numpy

def to_lambda(expr, constants):
    ''' Convert sympy expression composed of x and constants to lambda.
        For compatability with curve_fit, the resulting python lambda
        uses numpy functions instead of python math functions.

        Note that all expressions are assumed to be functions of at least x,
        so the constants list should not contain Symbol('x').

        expr - sympy symbolic expression composed of x and constants
        constants - list of constants (e.g. [c0, c1])
    '''
    return sympy.lambdify([sympy.symbols('x')] + constants, expr,
                          modules="numpy")

def sse(f, x_data, y_data):
    ''' Helper function for sym_fit. Return error for function f.
        f must be a unary python function. *_data must be numpy arrays.
    ''' 
    return ((f(x_data) - y_data)**2).sum()
    
def sym_fit(expr, constants, x_vals, y_vals, guesses=None):
    ''' Fit sympy expression expr of x and constants to vals.
        Return (optimal_fit, sum_squares_error)
        If no fit can be found, sse will be either a numpy inf or nan.
        
        TODO: guesses will perform multiple curve_fits with different
        initial values (N(0, max(x_vals, y_vals)) and return the best.
    '''
    f = to_lambda(expr, constants)
    x_data = numpy.array(x_vals)
    y_data = numpy.array(y_vals)
   
    # no vars to fit
    if len(constants) == 0:
        return ([], sse(f, x_data, y_data))

    popt, pcov = scipy.optimize.curve_fit(f, x_data, y_data)
    f_opt = lambda x: f(x, *popt)
    err = sse(f_opt, x_data, y_data)

    return (popt, err)


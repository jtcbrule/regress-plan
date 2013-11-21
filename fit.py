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
    
    guesses>0 will perform multiple curve_fits with different
    initial values drawn from (N(0, abs(x_data).max() * 1.5) and return the best.
    (This gives approximately a 50% chance the param will be within the range
     of the x vals and 50% the param will be outside the range of x_vals)
    '''
    f = to_lambda(expr, constants)
    x_data = numpy.array(x_vals)
    y_data = numpy.array(y_vals)
   
    # no vars to fit
    if len(constants) == 0:
        return ([], sse(f, x_data, y_data))

    # no guesses: 1 for all parameters, fit and return
    if not guesses:
        popt, pcov = scipy.optimize.curve_fit(f, x_data, y_data)
        f_opt = lambda x: f(x, *popt)
        err = sse(f_opt, x_data, y_data)
        return (popt, err)
    
    # multiple guesses
    min_err = numpy.inf
    min_popt = numpy.ones(len(constants))
    for i in range(0, guesses):
        # run a fit with a guess
        guess = numpy.random.randn(len(constants)) * numpy.abs(x_data).max() * 1.5
        popt, pcov = scipy.optimize.curve_fit(f, x_data, y_data, guess)
        f_opt = lambda x: f(x, *popt)
        err = sse(f_opt, x_data, y_data)
        
        if err < min_err:
            min_err = err
            min_popt = popt
            
    return (min_popt, min_err)

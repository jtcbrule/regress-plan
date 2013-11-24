''' "Physicist" search
'''

import numpy 
import sympy

import operations as ops

import fit
import exptree
import random

''' Convention: j, k are constants for prototypes'''
x, c, j, k = sympy.symbols('x c j k')

'''List of function prototypes and their constants'''
prototypes = [ops.sqrt(x + j), ops.log(x + j), ops.exp(x*j)]


def cross_multiply(x, y):
    '''Given two lists, return a list of all possible products x[i] * y[j]
    where i != j.
    '''
    return [i * j for i in x for j in y if i != j]


def physics_fit(prototypes, x_data, y_data, threshold=1, max_terms=None,
                fit_tries=3, epsilon=0, mul_depth=1):
    '''Do a "physicist fit"
    prototypes - list of base functions
    x_data, y_data - data to fit
    threshold - stop when fit error is below threshold
    max_terms - stop when model has this many potototype functions
    epsilon - probability of choosing non-optimal term
    mul-depth - generates more prototypes by cross_multipying
    '''

    # TODO: cross_multiply mul_depth times
   
    # calculate error levels for every function prototype
    error_level = []
    for func in prototypes:
        # add a leading constant for better fitting
        func_plus_const = func + c
        constants = func_plus_const.free_symbols 
        constants.remove(x) 
        constants = list(constants)

        opt, err = fit.sym_fit(func_plus_const, constants, x_data, y_data, fit_tries)
        if err < numpy.inf:
            error_level.append((err, func))
    
    return error_level

def main():
    pass

if __name__ == "__main__":
    main()


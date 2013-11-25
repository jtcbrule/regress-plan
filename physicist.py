#!/bin/env python3

''' "Physicist" search
'''

import numpy 
import sympy

import operations as ops

import fit
import exptree
import random

x = sympy.symbols('x')

''' Convention: j, k are constants for prototypes'''
j, k = sympy.symbols('j k')

'''List of function prototypes and their constants'''
basic_functions = [x, x**2, ops.sqrt(x + j), ops.log(x + j), ops.exp(x*j), ops.sin(x*j +k)]


def cross_multiply(x, y):
    '''Given two lists, return a list of all possible products x[i] * y[j]
    where i != j.
    '''
    return [i * j for i in x for j in y if i != j]

def rename_constants(prototype, cur_constants):
    '''Rename the constants in prototype expression to avoid name collisions.
    Returns renamed prototype; cur_constants is updated in-place.
    '''
    prototype_constants = list(prototype.free_symbols)
    prototype_constants.remove(x)

    j = len(cur_constants)
    k = len(prototype_constants)
    new_constants = [sympy.symbols('c' + str(i)) for i in
                     range(j, j + k)]
    
    cur_constants.extend(new_constants)
    return prototype.subs(zip(prototype_constants, new_constants))

def physics_fit(prototypes, x_data, y_data, threshold=1, max_terms=None,
                fit_tries=3, mul_depth=1, epsilon=0):
    '''Do a "physicist fit"
    prototypes - list of base functions
    x_data, y_data - data to fit
    threshold - stop when fit error is below threshold
    max_terms - stop when model has this many potototype functions
    mul-depth - generates more prototypes by cross_multipying
    epsilon - probability of choosing non-optimal term
    '''

    # TODO: cross_multiply mul_depth times

    # zero-order model
    c0 = sympy.symbols('c0')
   
    # calculate error levels for every function prototype
    base_score = []
    for func in prototypes:
        # add a leading constant for better fitting
        func_plus_const = func + c0
        constants = func_plus_const.free_symbols 
        constants.remove(x) 
        constants = list(constants)

        opt, err = fit.sym_fit(func_plus_const, constants, x_data, y_data,
                               guesses=fit_tries)

        if err < numpy.inf:
            base_score.append((err, func))
    
    base_score = sorted(base_score, key=lambda x: x[0], reverse=True)
    
    model_constants = [c0]
    model = c0
    opt, cur_err = fit.sym_fit(model, model_constants, x_data, y_data)

    print("Baseline error:", cur_err) #TODO remove
     
    if max_terms==None: max_terms = len(prototypes) 

    for i in range(0, max_terms):
        if cur_err < threshold: break
        
        # update model with best scoring prototype and re-fit
        best_expr = base_score.pop()[1]
        model += rename_constants(best_expr, model_constants)
        opt, cur_err = fit.sym_fit(model, model_constants, x_data, y_data,
                                   fit_tries)

        # TODO remove
        print("Current Model:", model, "Error:", cur_err)

    return (model, opt, cur_err)

def main():
    pass

if __name__ == "__main__":
    main()


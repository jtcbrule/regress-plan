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

''' Note: prototype functions CAN NOT use ci (for int i) constant names'''
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

    WARNING: unsafe to call on prototype expression with constants of the form
    ci (for int i)
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
                fit_tries=6, mul_depth=1, epsilon=0):
    '''Do a "physicist fit"
    prototypes - list of base functions
    x_data, y_data - data to fit
    threshold - stop when fit error is below threshold
    max_terms - stop when model has this many potototype expressions
    mul-depth - generates more prototypes by cross_multipying (unimplemented)
    epsilon - probability of choosing non-optimal term (unimplemented)
    '''
    
    debug_info = []

    # TODO: cross_multiply mul_depth times
    # TODO: epsilon-greedy strategy

    # zero-order and first-order models
    c0, c1 = sympy.symbols('c0 c1')
   
    # calculate error levels for every function prototype
    base_score = []
    for func in prototypes:
        # add leading constants for better fitting
        func_plus_const = c1 * func + c0
        constants = func_plus_const.free_symbols 
        constants.remove(x) 
        constants = list(constants)

        opt, err = fit.sym_fit(func_plus_const, constants, x_data, y_data,
                               guesses=fit_tries)

        if err < numpy.inf:
            base_score.append((err, func))
        
        debug_info.append((func_plus_const.subs(zip(constants, opt)),err))
    
    base_score = sorted(base_score, key=lambda x: x[0], reverse=True)
    
    model_constants = [c0]
    model = c0
    opt, cur_err = fit.sym_fit(model, model_constants, x_data, y_data)

    debug_info.append((c0.subs(c0,opt),cur_err))
     
    if max_terms==None: max_terms = len(prototypes) 

    for i in range(0, max_terms):
        if cur_err < threshold: break
        
        # grab the best_scoring expression
        best_expr = base_score.pop()[1]

        # rename constants to avoid name collisions
        best_expr = rename_constants(best_expr, model_constants)
        
        # every prototype term gets a leading multiplicative constant
        model_constants.append(sympy.symbols('c' + str(len(model_constants))))
        best_expr *= model_constants[-1]
       
        # refit
        model += best_expr
        opt, cur_err = fit.sym_fit(model, model_constants, x_data, y_data,
                                   fit_tries)
        
        debug_info.append((model.subs(zip(model_constants, opt)), cur_err))

    return debug_info

def main():
    import data
    
    x_data = range(1, 25 + 1)
    
    info = physics_fit(basic_functions, x_data, data.identity, threshold = 25)
    
    for i in info:
        print(i)

    print("----")
    info = physics_fit(basic_functions, x_data, data.bullet, threshold = 25)
    for i in info:
        print(i)

if __name__ == "__main__":
    main()


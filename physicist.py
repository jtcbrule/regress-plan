#!/bin/env python3

''' "Physicist" search
'''

import numpy 
import sympy

import operations as ops

import fit
import exptree
import random

import functools
import itertools

x = sympy.symbols('x')

''' Note: prototype functions CAN NOT use ci (for int i) constant names'''
j, k, l, m, n, o, p = sympy.symbols('j k l m n o p')

'''List of function prototypes and their constants'''
basic_functions = [x, x**2, ops.sqrt(x + j), ops.log(x + k), ops.exp(x*l), ops.sin(x*m +n), ops.atan(x*o + p)]


def cross_multiply(l, k):
    '''Given a list, return a list of all possible product combinations
    (Up to k)
    '''
    result = l 
    for i in range(2, k + 1):
        if i > len(l): break

        combos = list(itertools.combinations(l, i))
        for j in range(0, len(combos)):
            combos[j] = functools.reduce(lambda x, y: x*y, combos[j])

        result = result + combos

    return result

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

def error_factor(constant, k):
    '''Regularization term for constants. Threads over lists.
    UNUSED 
    '''
    error = (k * numpy.log(numpy.abs(constant) + 1) - 1)
    return 1 + numpy.clip(error, 0, numpy.finfo('d').max)

def physics_fit(prototypes, x_data, y_data, threshold=0, max_terms=5,
                fit_tries=12, mul_depth=2):
    '''Do a "physicist fit"; expects standard score normalized data
    prototypes - list of base functions
    x_data, y_data - data to fit
    threshold - stop when fit error is below threshold
    max_terms - stop when model has this many potototype expressions
    mul-depth - generates more prototypes by cross_multipying (unimplemented)
    '''
    
    debug_info = []

    prototypes = cross_multiply(prototypes, mul_depth)

    c0, c1 = sympy.symbols('c0 c1')

    # zero order model
    opt, cur_err = fit.sym_fit(c0, [c0], x_data, y_data)
    zero_order = opt[0]
    zero_order_error = cur_err
    
    debug_info.append("Zero order model:")
    debug_info.append((zero_order, cur_err))

    debug_info.append("prototype scores:")
    # calculate base error levels for every function prototype
    base_score = []
    for func in prototypes:
        # multiply by constant for better fitting, rename
        func_times_const = c1 * func + c0
        constants = func_times_const.free_symbols 
        constants.remove(x) 
        constants = list(constants)
        
        # fit data
        opt, err = fit.sym_fit(func_times_const, constants, x_data,
                               y_data, fit_tries * len(constants))
        
        if err < numpy.inf:
            base_score.append((err, func))
        
        #debug_info.append((func_times_const.subs(zip(constants, opt)),err))
    
    base_score = sorted(base_score, key=lambda x: x[0], reverse=True)

    for i in base_score:
        debug_info.append((i[1], i[0]))
   
    debug_info.append("Modeling execution trace:")
    # start modeling
    model = c0
    model_constants = [c0]
    for i in range(0, max_terms):
        if cur_err < threshold: break
        
        # grab the best_scoring expression
        best_expr = base_score.pop()[1]
        
        # rename constants to avoid name collisions
        best_expr = rename_constants(best_expr, model_constants)
        
        # every prototype term gets a leading multiplicative constant
        model_constants.append(sympy.symbols('c' +
                               str(len(model_constants))))
        best_expr *= model_constants[-1]
        
        # refit
        model += best_expr
        opt, cur_err = fit.sym_fit(model, model_constants, x_data, y_data,
                                   fit_tries * len(model_constants))
        
        debug_info.append((model.subs(zip(model_constants, opt)), cur_err))

        # break if you start doing worse than zero-order model
        if cur_err > zero_order_error: break

    return debug_info

def normalize(arr):
    '''Normalize a numpy array'''
    return (arr - arr.mean()) / arr.std()

def main():
    import data
    
    x_data = numpy.array(range(1, 25 + 1)) 
    x_data = normalize(x_data)
    
    print("Identity:")
    y_data = numpy.array(data.identity)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)

    print("Bullet:")
    y_data = numpy.array(data.bullet)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)

    print("Oscillator")
    y_data = numpy.array(data.oscillator)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("Half Life")
    y_data = numpy.array(data.half_life)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("Enzyme")
    y_data = numpy.array(data.enzyme)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("Fibonacci")
    y_data = numpy.array(data.fibonacci)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("Population")
    y_data = numpy.array(data.population)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    x_data = numpy.array(range(0, 100)) 
    x_data = normalize(x_data)
    
    print("Hubbert")
    y_data = numpy.array(data.hubbert)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
    
    print("US GDP")
    y_data = numpy.array(data.us_gdp)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("US population")
    y_data = numpy.array(data.us_pop)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)
        
    print("IQ curve")
    y_data = numpy.array(data.iq)
    y_data = normalize(y_data)
    info = physics_fit(basic_functions, x_data, y_data)
    for i in info:
        print(i)

if __name__ == "__main__":
    main()

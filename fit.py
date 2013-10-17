#!/bin/env python3
from sympy import symbols, lambdify
from scipy.optimize import curve_fit
import numpy as np

# maximum number of constants in a symbolic expression
MAX_CONSTANTS = 10

# symbolical constants/variable (note that c[0] = x)
x = symbols('x')
c = list(symbols('c1:' + str(MAX_CONSTANTS)))
c.insert(0, x)

def to_lambda(expr, num_param):
    """ Return a (python) lambda expression 

        expr - symbolic expression composed of x and c1...ck
        num_param - number of parameters (e.g. f(x; c1, c2) has 2 params)
        
        Note that expr cannot contain constant ck for k > num_param
    """
    return lambdify(c[:(num_param + 1)], expr)


sample_expr = c[1] * x**2 + c[2]

# 2 * x^2 + 1
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 3, 9, 19, 33, 51]) #exact
y_err = np.array([1.1, 3.1, 8.9, 19.8, 33.1, 50]) #with some error
guess = np.array([1.0, 1.0]) #optional

f = to_lambda(sample_expr, 2)

# note that trace(cov) is equal to mse for unbiased estimators
# also, note that curve_fit requires numpy arrays
popt, pcov = curve_fit(f, x_data, y_data)
print("Fit to y_data")
print(popt)
print(np.sum(np.diag(pcov)))

popt, pcov = curve_fit(f, x_data, y_err)
print("Fit to y_err")
print(popt)
print(np.sum(np.diag(pcov)))

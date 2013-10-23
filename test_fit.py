#!/bin/env python3
'''
test_fit.py
Example file demonstrating how to fit symbolic expressions using scipy
'''

import sympy
from scipy.optimize import curve_fit
import numpy as np
from fit import to_lambda

x, c0, c1 = sympy.symbols("x c0 c1")

sample_expr = c1 * x**2 + c0

# 2 * x^2 + 1
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 3, 9, 19, 33, 51]) #exact
y_err = np.array([1.1, 3.1, 8.9, 19.8, 33.1, 50]) #with some error
guess = np.array([1.0, 1.0]) #optional initial guess

f = to_lambda(sample_expr, [c0, c1])

print("Attempting to fit c1 * x^2 + c2")

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

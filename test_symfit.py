#!/bin/env python3
'''
test_symfit.py
Examples of using the sym_fit() wrapper function from fit.py
'''

from sympy import symbols
from fit import sym_fit
import operations as ops

x, c0, c1, c2 = symbols("x c0 c1 c2")

expr = c1 * x**2 + c0

# 2 * x^2 + 1
x_data = [0, 1, 2, 3, 4, 5]
y_data = [1, 3, 9, 19, 33, 51] #exact
y_err = [1.1, 3.1, 8.9, 19.8, 33.1, 50] #with some error

print("Attempting to fit c1 * x^2 + c2")

popt, err = sym_fit(expr, [c0, c1], x_data, y_data)
print("Fit to y_data")
print(popt)
print(err)

popt, err = sym_fit(expr, [c0, c1], x_data, y_err)
print("Fit to y_err")
print(popt)
print(err)

print("")

x_data = [1, 2, 3, 4, 5]
y_data = [3, 9, 19, 33, 51]
expr = c0

print("Attempting to fit just c0")

popt, err = sym_fit(expr, [c0], x_data, y_data)
print("Fit to y_data")
print(popt)
print(err)

print("")

x_data = [1, 2, 3, 4, 5]
y_data = [3, 9, 19, 33, 51]
expr = x

print("'fit' just x (no free parameters)")

popt, err = sym_fit(expr, [], x_data, y_data)
print("Fit to y_data")
print(popt)
print(err)

print("---")

x_data = range(-10, 10)
y_data = range(-10, 10)
expr = ops.log(x + c0) + c1

print("Attempting to c1 * log(x + c0) + c2 (multiple guesses)")

popt, err = sym_fit(expr, [c0, c1], x_data, y_data, 12)
print("Fit to y_data")
print(popt)
print(err)

print("")

x_data = [-1, 1, 2, 3]
y_data = [1, 2, 3, 4]
expr = ops.log(x) + c0

print("Attempting to log(x) + c0 (should fail on this domain)")

popt, err = sym_fit(expr, [c0], x_data, y_data)
print("Fit to y_data")
print(popt)
print(err)
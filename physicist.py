''' "Physicist" search
'''

import numpy as np
import sympy

import operations as ops

import fit
import exptree
import random

x, j, k = sympy.symbols('x')

'''List of function prototypes and their constants'''
prototypes = [ops.sqrt(x + j), ops.log(x + j), ops.sin(i*), ops.exp(x*j)]


def cross_multiply(x, y):
    '''Given two lists, return a list of all possible products x[i] * y[j]
    where i != j.
    '''
    return [i * j for i in x for j in y if i != j]


def physics_fit(prototypes, threshold, max_terms, epsilon=0, mul_depth=1):
    '''Do a "physicist fit"
    prototypes - list of base functions
    threshold - stop when fit error is below this
    max_terms - maximum number of base function terms
    epsilon - probability of choosing non-optimal term
    mul-depth - generates 
    '''

    # TODO: cross_multiply mul_depth times

    


def main():
    pass

if __name__ == "__main__":
    main()


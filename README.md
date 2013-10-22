regress-plan
============

Notes
-----

### Divide by zero and infinity ###

Some of the symbolic expressions might result in a divide by zero. Sympy converts these expressions to +inf, -inf or nan as appropriate. To use curve_fit, we can either throw exceptions, or wrap the functions with:

    numpy.nan_to_num()

### Weighted probabilistc search ###

A search strategy that may be worth exploring: define the measure of how much we 'want' to expand a certain path represented as a probability vector. Some functions are likely to appear in regression (polynomials), others (e.g. arctan) shouldn't pop up that often.

Dependencies
------------

* python3
* numpy
* scipy (library)
* sympy

Sympy
-----

Quirks of the sympy library:

http://docs.sympy.org/latest/tutorial/gotchas.html
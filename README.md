regress-plan
============

Files/TODO
----------

* exptree.py - symbolic expression trees; **TODO:** implement __deepcopy__()
* term.py - individual nodes for an ExpTree()
* operations.py - sympy-compatible functions **TODO:** add all elementary functions
* fit.py - utility functions for curve fitting sympy expressions; **TODO:**
    * write wrapper around scipy.optimize.curve_fit for fitting symbolic expressions
    * write fitting function to try multiple random initial guesses
    * write function to do a zero-order fit (constant function) and linear fit and report MSE ('baseline' error levels)

* test_fit.py - example of curve fitting using the scipy.optimize library
* test_term.py - example of using ExpTree()'s functions

**TODO:** Write unit tests.

**TODO:** Start implementing various search strategies. Recommend one file per search-strategy.

Notes/Ideas
-----------

### Divide by zero and infinity ###

Some of the symbolic expressions might result in a divide by zero. Sympy converts these expressions to +inf, -inf or nan as appropriate. To use curve_fit, we can either throw exceptions, or wrap the functions with:

    numpy.nan_to_num()

### Weighted probabilistc search ###

A search strategy that may be worth exploring: define the measure of how much we 'want' to expand a certain path represented as a probability vector. Some functions are likely to appear in regression (polynomials), others (e.g. arctan) shouldn't pop up that often.

### "Physicist" search ###

Symbolic expressions composed of the addition of pre-built functions only. Inspired by:

http://xkcd.com/793/

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
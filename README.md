regress-plan
============

Files/TODO
----------

* exptree.py - symbolic expression tree;
* term.py - individual nodes for an ExpTree()
* operations.py - collection of sympy-compatible functions;
* fit.py - utility functions for curve fitting sympy expressions; **TODO:**
    * improve sym_fit() to allow for multiple initial random guesses (initial guesses based on data?)

* test.py - unit tests; **TODO:** better unittests (current code coverage is terrible)
    
* test_symfit.py - example of symbolic curve fitting with wrapper functions
* test_fit.py - example of curve fitting using the scipy.optimize library
* test_term.py - example of using ExpTree()'s functions

**TODO:** Start implementing various search strategies. Recommend one file per search-strategy.

Notes/Ideas
-----------

### Domain restrictions and multiple guesses ###

Fitting a function like log(x + c0) can lead to non-fits (sym_fit() returns nan) if initial guess puts log() outside of its defined domain. One way to solve this is with multiple initial guess on the fitting function. (By default, the initial guess for all parameters is 1.) In the mean time, just use data with nothing but positive domains.

### operations.py and exptree.py ##

Powers (x^c) are approximately represented in the search space via repeated multiplication and square roots.

Trigonometric functions are over-represented (sin, cos, tan can be expressed in terms of each other), but this may be a better search space. Smiliarily, sub() may be redundant.

Inverse trigonometric functions are fully represented (arcsin and arccos are elementary functions of arctan); arctan was the only one included since it's domain is entire real line.

### Weighted probabilistc search ###

A search strategy that may be worth exploring: define the measure of how much we 'want' to expand a certain path represented as a probability vector. Some functions are likely to appear in regression (polynomials), others (e.g. arctan) shouldn't pop up that often.

### "Physicist" search ###

Symbolic expressions composed of the addition of pre-built functions only. Inspired by:

http://xkcd.com/793/

Dependencies
------------

* python3
* numpy
* scipy (library, not the full stack)
* sympy

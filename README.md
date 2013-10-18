regress-plan
============

"Gotchas"
---------

Probably worth reading to understand some quirks of the sympy library:

http://docs.sympy.org/latest/tutorial/gotchas.html

Notes
-----

Search strategy may include a certain probabilistic element: the measure of how much we 'want' to expand a certain path may be nicely represented as a probability. Some functions are likely to appear in regression (polynomials), others (e.g. arctan) shouldn't pop up that often.

### On using the term class ###

Note that in the Term class, the leaves of the tree represent the variable 'x', and that all the internal nodes are unary or binary functions. *Constants* aren't directly represented *anywhere* in the tree.

This is intentional. In addition to the elementary functions, we can have two special unary functions "+c" and "*c" which correspond to adding or multiplying by a (unique) constant at that term. This eleminates a lot of redundant possible term-trees, for example adding or subtracting a constant is equivalent, as is multiplying or dividing by a constant.

Dependencies
------------

* python3
* numpy
* scipy (library)
* sympy


#!/bin/env python3
from sympy import symbols
from sympy.utilities.lambdify import implemented_function

#wrappers for the field operations
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

class Term:
    """ A Term is a symbolic expression as a tree, defined recursively.
        
        An *empty* Term is just Symbol('x'). op is a unary or binary
        *sympy* function wih lhs and rhs being the 1st and 2nd args.
        Since op is a function +, -, *, / must be wrapped as add(), etc

        sympy functions are in sympy.core.function.elementary

        Note that a single symbolic expression can have multiple Term
        representations. For example x + sin(x) == sin(x) + x, but these
        have different Term tree forms.

        TODO: implement a 'leaves' function that returns a collection of
        all the leaves of the tree to make it easier to expand the tree
    """

    def __init__(self, op=None, lhs=None, rhs=None):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def collapse(self):
        """Collapse the tree into a sympy symbolic expression"""
        if self.op == None: #empty term
            return symbols('x')
        elif self.rhs == None: #unary function
            return self.op(self.lhs.collapse())
        else: #binary function
            return self.op(self.lhs.collapse(), self.rhs.collapse())

    def __repr__(self):     
        """The tree as an s-expression"""
        if self.op == None:
            return "x"
        elif self.rhs == None:
            return "(" + str(self.op) + " " + str(self.lhs) + ")"
        else:
            if self.op == add:
                op_str = '+'
            elif self.op == sub:
                op_str = '-'
            elif self.op == mul:
                op_str = '*'
            elif self.op == div:
                op_str = '/'
            else:
                op_str = str(self.op) #shouldn't happen
            
            return ("(" + str(op_str) + " " + str(self.lhs) + " " +
                    str(self.rhs) + ")")

    def __str__(self):
        return repr(self)

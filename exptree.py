import operations as ops
from term import Term
import random
from sympy import symbols

class ExpTree:

    def __init__(self):
        self.root = Term() # Root of tree
        self.leaves = [self.root] # Bottom level terms
        self.constants = [] # Names of constants

    def get_random_leaf(self):
        return random.choice(self.leaves)

    def __str__(self):
        return str(self.root)

    def apply_unary_op(self, term, op):
        ''' Apply a unary operation to a given term. This should only
            be called on leaves, so this can just set the op of the current
            term and then create a new Term() as a LHS child '''
        assert term.lhs is None and term.rhs is None
        term.op = op
        term.lhs = Term()

    def apply_binary_op(self, term, op):
        ''' Apply a binary operation to the given term. '''
        assert term.lhs is None and term.rhs is None
        term.op = op
        term.lhs = Term()
        term.rhs = Term()

    def apply_constant_op(self, term, op):
        ''' Apply one of the constant operations (add or multiply by a
            constant) to the given term. '''
        assert term.lhs is None and term.rhs is None
        c = symbols('c' + str(len(self.constants)))
        term.op = op(c)
        self.constants.append(c)
        term.lhs = Term()
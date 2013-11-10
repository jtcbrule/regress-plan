from term import Term
import random
from sympy import symbols
import copy

class ExpTree:
    ''' A wrapper class around a Term tree.
        Keeps track of leaf terms and symbolic constants.
        
        The .apply_ functions modify the tree in place.
        Use .copy() to get a deep copy of the tree.

        self.root - the root Term
        self.leaves - list of leaf Terms
        self.constants - list of symbolic constants
    '''

    def __init__(self):
        self.root = Term() # Root of tree
        self.leaves = [self.root] # Bottom level terms
        self.constants = [] # List of constants

    def copy(self):
        return copy.deepcopy(self)

    def get_random_leaf(self):
        return random.choice(self.leaves)

    def __str__(self):
        return str(self.root)

    def to_expr(self):
        ''' Return the sympy expression this exptree represents '''
        return self.root.collapse()

    def apply_unary_op(self, term, op):
        ''' Apply unary operation op to leaf term and update self.leaves
            Only callable on a leaf term.

            Returns the new leaf.
        '''
        assert term.lhs is None and term.rhs is None
        term.op = op
        term.lhs = Term()
        self.leaves.remove(term)
        self.leaves.append(term.lhs)

        return term.lhs

    def apply_binary_op(self, term, op):
        ''' Apply binary operation op to leaf term and update self.leaves
            Only callable on a leaf term.

            Returns the two new leaves as a tuple.
        '''
        assert term.lhs is None and term.rhs is None
        term.op = op
        term.lhs = Term()
        term.rhs = Term()
        self.leaves.remove(term)
        self.leaves.append(term.lhs)
        self.leaves.append(term.rhs)

        return (term.lhs, term.rhs)

    def apply_plus_c(self, term):
        ''' Apply a 'plus constant' op to leaf term; update self.leaves
            Only callable on a leaf term.

            Returns the new leaf.
        '''
        assert term.lhs is None and term.rhs is None

        # generate unique constant symbol; update constant list
        c = symbols('c' + str(len(self.constants)))
        self.constants.append(c)

        # expand leaf term
        term.op = lambda x: x + c
        term.op.__name__ = '+' + str(c)
        term.lhs = Term()

        self.leaves.remove(term)
        self.leaves.append(term.lhs)

        return term.lhs

    def apply_times_c(self, term):
        ''' Apply a 'times constant' op to leaf term; update self.leaves
            Only callable on a leaf term.

            Returns the new leaf.
        '''
        assert term.lhs is None and term.rhs is None

        # generate unique constant symbol; update constant list
        c = symbols('c' + str(len(self.constants)))
        self.constants.append(c)

        # expand leaf term
        term.op = lambda x: x * c
        term.op.__name__ = '*' + str(c)
        term.lhs = Term()

        self.leaves.remove(term)
        self.leaves.append(term.lhs)

        return term.lhs

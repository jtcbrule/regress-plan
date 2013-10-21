'''
Testing the expression tree and generating expression trees
'''

import operations as ops
from term import Term

import random


class ExpTree:



    def __init__(self):
        self.root = Term()
        self.leaves = [self.root]

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
        assert term.lhs is None and term.rhs is None
        term.op = op
        term.lhs = Term()
        term.rhs = Term()




def generate_expressions():

    tree = ExpTree()
    leaves = [tree]

    print "initial tree: " + str(tree)
    print "making a change..."

    tree.apply_binary_op(tree.root, ops.add)

    print "modified tree: " + str(tree.root.collapse())




def main():
    generate_expressions()

if __name__ == "__main__":
    main()
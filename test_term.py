'''
Testing the expression tree and generating expression trees
'''

# TODO: fix this file, now that changes to exptree have been made.

import operations as ops
from exptree import ExpTree



def generate_expressions():

    tree = ExpTree()
    leaves = [tree]

    print "initial tree: " + str(tree)
    print "making a change..."

    tree.apply_constant_op(tree.root, ops.add_constant)

    print "modified tree: " + str(tree.root.collapse())




def main():
    generate_expressions()

if __name__ == "__main__":
    main()
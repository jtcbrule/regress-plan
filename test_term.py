'''
Testing the expression tree and generating expression trees
'''

import operations as ops
from exptree import ExpTree

def example_tree():

    tree = ExpTree()
    leaf = tree.leaves[0]
    print("initial tree: " + str(tree))

    leaf = tree.apply_times_c(leaf)
    print("expanded with apply_times_c(): " + str(tree))

    leaf = tree.apply_plus_c(leaf)
    print("expanded with apply_plus_c(): " + str(tree))

    left_leaf, right_leaf = tree.apply_binary_op(leaf, ops.mul)
    print("expanded with apply_binary_op(mul): " + str(tree))

    tree.apply_unary_op(left_leaf, ops.sin)
    print("expanded left leaf with apply_unary_op(sin): " + str(tree))

    tree.apply_unary_op(right_leaf, ops.log)
    print("expanded right leaf with apply_unary_op(log): " + str(tree))

    expr = tree.to_expr()
    print("tree as sympy expression: " + str(expr))

    print("number of leaves: " + str(len(tree.leaves)))
    print("constants: " + str(tree.constants))

def main():
    example_tree()

if __name__ == "__main__":
    main()

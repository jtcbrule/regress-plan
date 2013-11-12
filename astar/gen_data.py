# Isaac Julien
# Generate data for testing


import sys
sys.path.append('../')

import operations as ops
from exptree import ExpTree

import sympy

import numpy as np
import random

class simple_generator:


    # num_points = number of data points, noise_level = standard deviation of noise
    def __init__(self, num_points, noise_level, max_const):

        # Maximum value of a constant in the expression
        self.MAX_CONST = max_const

        # Dictionary of operations -> data
        self.ops_to_data = {}

        # Array of noise values with std dev = noise_level
        noise = np.random.normal(0,noise_level,num_points)

        equation = None;

        self.all_ops = ops.unary_ops + ops.binary_ops
        # Probability of choosing the "+c" or "*c" option
        self.p_addc = 1 / float(len(self.all_ops) + 2)


    # Generate a random expression tree, up to a max depth:
    def generate_random_exptree(self, depth):
        tree = ExpTree()
        d = 0
        while (d < depth):

            # Make SHALLOW copy of leaves array:
            to_expand = []
            for leaf in tree.leaves:
                to_expand.append(leaf)

            for leaf in to_expand:

                # Apply +c or *c possibly:
                r = random.random()
                if r < self.p_addc:
                    tree.apply_plus_c(leaf)
                elif r < 2 * self.p_addc:
                    tree.apply_times_c(leaf)


                # Otherwise, choose a unary or binary op:
                else:
                    op = random.choice(self.all_ops);
                    if op in ops.unary_ops:
                        tree.apply_unary_op(leaf, op)
                    else:
                        tree.apply_binary_op(leaf, op)
            d += 1

        return tree



    # Generate a list of constants for an expression tree:
    def generate_constants(self, exptree):
        consts = []
        for i in range(len(exptree.constants)):
            consts.append(random.randint(1, self.MAX_CONST))
        return consts



    def generate_data_points(self, exptree, num_points):
        pass




def main():
    gen = simple_generator(1, 1, 10)
    tree = gen.generate_random_exptree(2)
    gen.generate_constants(tree)


    lambda_exp = to_lambda(tree.root.collapse(), tree.constants)
    constants = gen.generate_constants(tree)

    print "expression = " + str(tree.root.collapse())
    print "constants = " + str(constants)

    for i in range(1,10):
        print i, '\t', lambda_exp(*([i]+constants))


def to_lambda(expr, constants):
    #print str([sympy.symbols('x')] + constants)
    #print expr
    return sympy.lambdify([sympy.symbols('x')] + constants, expr)



if __name__ == "__main__":
    main()


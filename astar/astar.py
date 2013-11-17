# Isaac Julien
# a-star

import sys
sys.path.append('../')

import operations as ops
from exptree import ExpTree
import random
from Queue import PriorityQueue

import gen_data, expand

from scipy.optimize import curve_fit
import numpy as np

''' Basic implementation of A* search '''
'''
Notes:
- No pruning or limitations on operations performed on leaves
- Interpreting error as h (measure of distance to goal)
'''
class AStar:


    '''
    Inner class represents an A* state.
    This is what the PQ will store.
    A state is an expression tree plus a score:
    '''
    class State:
        def __init__(self, exptree, score):
            self.exptree = exptree
            self.score = score


    '''
    Input = lists of x and y coordinates
    '''
    def __init__(self, X, Y):

        self.X = X
        self.Y = Y

        self.THRESH = .01

        exptree = ExpTree()

        self.states = PriorityQueue()
        self.states.put(exptree)

        done = False
        while not done:

            # Choose state to expand:
            to_expand = self.states.get()

            print "Expanding the expression: " + str(to_expand.root.collapse())
            children = expand.expand(to_expand)
            temp = set()
            for child in children:

                try:
                    score = self.score(child)
                    if score < self.THRESH:
                        print "Found solution! " + str(child.root.collapse()) + " Var: " + str(score)
                        return
                except:
                    print "\t" + str(child.root.collapse())
                    print '\t\t' + "Failed!"
                    continue

                print '\t' + str(child.root.collapse())
                print '\t\t' + str(score)
                temp.add(child)

            children = temp
            for child in children:
                self.states.put(child)

    '''
    Return a score for the fit of exptree on x and y
    '''
    def score(self, exptree):

        lambda_exp = exptree.to_lambda();
        popt, pcov = curve_fit(lambda_exp, self.X, self.Y)
        return np.sum(np.diag(pcov))




def main():
    print "Getting data..."
    tree, constants, x, y = gen_data.get_single_expression_and_data()
    print "Got 1000 points with 0 error for expression: " + str(tree.root.collapse())

    print "Beginning A*..."
    astar = AStar(x, y)

if __name__ == "__main__":
    main()
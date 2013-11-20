# Isaac Julien
# a-star

import sys
sys.path.append('../')

import operations as ops
from exptree import ExpTree
import random
from Queue import PriorityQueue

import gen_data, expand, fit

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
    A state in the search space
    '''
    class AStarState:
        def __init__(self, exptree, score, depth):
            self.exptree = exptree
            self.score = score
            self.depth = depth


    '''
    Input = lists of x and y coordinates
    '''
    def __init__(self, X, Y, draw_graph=False):



        # LEARN EXPANSION 'RULES' based on HOW MUCH THE ERROR IMPROVES


        # Log guesses
        logfile = open("./guesses", 'w')

        self.X = X
        self.Y = Y

        self.THRESH = .01
        self.MAX_DEPTH = 2;

        exptree = ExpTree()
        init_state = AStar.AStarState(exptree, float("inf"), 0)

        self.states = PriorityQueue()
        self.states.put((init_state.score, init_state))


        while True:

            # Choose state to expand:
            try:
                state_to_expand = self.states.get(False)[1]
            except:
                print "Could not find any more states to expand"
                break

            expr_to_expand = state_to_expand.exptree
            expr_str = str(expr_to_expand.root.collapse())

            print "Expanding the expression: " + expr_str + " with score " + str(state_to_expand.score)

            '''
            ++++++++++++++++++++++++++++++++++ This is where the expansion happens: +++++++++++++++++++++++++++++++++++
            '''
            children = expand.expand(expr_to_expand)
            '''
            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            '''

            temp = set()
            for child in children:

                logfile.write(expr_str + '\t' + str(child.root.collapse()))
                logfile.write('\n')
                logfile.flush()

                try:

                    fit_constants, score = self.score(child.root.collapse(), child.constants)
                    child_depth = state_to_expand.depth + 1

                    if score < self.THRESH:

                        print "Found solution! " + str(child.root.collapse())
                        print "\tError: " + str(score)
                        print "\tFitted constants: " + str(fit_constants)
                        print
                        return

                    print '\t' + str(child.root.collapse())
                    print '\t\t' + str(score)

                    if child_depth >= self.MAX_DEPTH:
                        print "Hit maximum depth"
                        continue

                    new_state = AStar.AStarState(child, score, child_depth)
                    temp.add(new_state)

                except:
                    print '\t' + str(child.root.collapse()) + "FAILED"

            for new_state in temp:
                print new_state.score
                self.states.put((new_state.score, new_state))




    '''
    Return a score for the fit of exptree on x and y
    '''
    def score(self, exptree, constants):
        return fit.sym_fit(exptree, constants, self.X, self.Y)





def main():
    print "Getting data..."
    expr_depth = 2
    tree, constants, x, y = gen_data.get_single_expression_and_data(expr_depth)
    print "Got 1000 points with 0 error for expression: " + str(tree.root.collapse())
    print "With constants: " + str(constants)
    print
    print "Beginning A*..."
    print
    print
    astar = AStar(x, y, False)

if __name__ == "__main__":
    main()
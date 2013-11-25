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

import matplotlib.pyplot as plt



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
        def __init__(self, exptree, score, depth, fit_consts):
            self.exptree = exptree
            self.score = score
            self.fit_consts = fit_consts
            self.depth = depth


    '''
    Input = lists of x and y coordinates
    '''
    def __init__(self, X, Y, draw_graph=False):

        # PLOT THE BEST ERROR OVER TIME!
        # LEARN EXPANSION 'RULES' based on HOW MUCH THE ERROR IMPROVES


        # Log guesses
        logfile = open("./guesses", 'w')

        self.X = X
        self.Y = Y

        self.THRESH = .01
        self.MAX_DEPTH = 10;

        self.guesses = 5 # Number of guesses per fit

        '''
        For plotting purposes:
        '''
        self.best_err = []



        exptree = ExpTree()
        init_consts, init_score = self.score(exptree, exptree.constants)
        init_state = AStar.AStarState(exptree, init_score, 0, init_consts)

        '''
        Minimum erro expression, in case we hit max_iter:
        '''
        min = init_state

        self.states = PriorityQueue()
        self.states.put((1, init_state))

        iter = 0

        while True:

            if iter > 100:
                print "Hit max iterations. Best so far: " + str(child.root.collapse())
                print "\tError: " + str(score)
                print "\tFitted constants: " + str(fit_constants)
                break
            iter += 1

            # Choose state to expand:
            try:
                state_to_expand = self.states.get(False)[1]
            except:

                print "Could not find any more states to expand"
                break

            expr_to_expand = state_to_expand.exptree
            expr_str = str(expr_to_expand.root.collapse())

            self.best_err.append(state_to_expand.score)


            print "EXPANDING:", expr_str, state_to_expand.fit_consts, state_to_expand.score

            '''
            ++++++++++++++++++++++++++++++++++ This is where the expansion happens: +++++++++++++++++++++++++++++++++++
            '''
            children = expand.expand(expr_to_expand)
            #children = expand.expand_two_levels(expr_to_expand)
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

                        self.best_err.append(score)
                        print "Found solution! " + str(child.root.collapse())
                        print "\tError: " + str(score)
                        print "\tFitted constants: " + str(fit_constants)
                        print
                        return

                    if child_depth >= self.MAX_DEPTH:
                        print "Hit maximum depth"
                        continue

                    new_state = AStar.AStarState(child, score, child_depth, fit_constants)
                    temp.add(new_state)

                    '''
                    Keeping track of the min state:
                    '''
                    if score < min.score:
                        min = new_state

                except:
                    print '\t' + str(child.root.collapse()) + "FAILED"

            for new_state in temp:

                print '\t', new_state.exptree.root.collapse(), "SCORE", new_state.score

                self.states.put((score, new_state))




    '''
    Return a score for the fit of exptree on x and y
    '''
    def score(self, exptree, constants):
        return fit.sym_fit(exptree, constants, self.X, self.Y, self.guesses)




def basic():
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

    err = astar.best_err
    plt.plot(range(len(err)), err)
    plt.axis([-.1, len(err)+1, -1, max(err)+1])
    #ax = plt.subplot(221)
    #ax.set_yscale("log")
    plt.show()


def problem_case():
    exptree = ExpTree()
    exptree.apply_binary_operation(exptree.root, operations.add)
    exptree.apply_binary_operation(exptree.leaves[0], operations.cos)
    exptree.apply_binary_operation(exptree.leaves[1], operations.sin)
    print exptree


def real_data():
    import data
    x = [x for x in range(1,26)]
    y = data.identity
    astar = AStar(x,y,False)



def main():
    problem_case()

if __name__ == "__main__":
    main()
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
from scipy.stats import gaussian_kde
import numpy as np

import matplotlib.pyplot as plt


import warnings
import math


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
    def __init__(self, X, Y, thresh=.1, max_iter=50, draw_graph=False):

        # PLOT THE BEST ERROR OVER TIME!
        # LEARN EXPANSION 'RULES' based on HOW MUCH THE ERROR IMPROVES


        # Log guesses
        logfile = open("./guesses", 'w')

        self.X = X
        self.Y = Y

        self.THRESH = thresh
        self.MAX_DEPTH = 10
        self.MAX_ITER = max_iter

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
        self.min = init_state

        self.states = PriorityQueue()
        self.states.put((1, init_state))

        iter = 0

        while True:

            if iter > self.MAX_ITER:
                print "Hit max iterations. Best so far: " + str(self.min.exptree.root.collapse())
                print "\tError: " + str(self.min.score)
                print "\tFitted constants: " + str(self.min.fit_consts)
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
            #children = expand.expand(expr_to_expand)
            children = expand.expand_smart_two_levels(expr_to_expand)
            '''
            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            '''

            temp = set()
            for child in children:

                #logfile.write(expr_str + '\t' + str(child.root.collapse()))
                #logfile.write('\n')
                #logfile.flush()

                try:

                    fit_constants, score = self.score(child.root.collapse(), child.constants)
                    if score < 0:
                        print "???"
                        return
                    child_depth = state_to_expand.depth + 1

                    if score < self.THRESH:

                        self.best_err.append(score)
                        self.min = AStar.AStarState(child, score, child_depth, fit_constants)
                        print "Found solution! " + str(child.root.collapse())
                        print "\tError: " + str(score)
                        print "\tFitted constants: " + str(fit_constants)
                        print
                        return

                    if child_depth >= self.MAX_DEPTH:
                        print "\tHit maximum depth"
                        continue

                    new_state = AStar.AStarState(child, score, child_depth, fit_constants)
                    temp.add(new_state)

                    '''
                    Keeping track of the min state:
                    '''
                    if score < self.min.score:
                        #print "min:", min.exptree.root.collapse(), score
                        self.min = new_state

                except:
                    print '\t' + str(child.root.collapse()) + "FAILED"

            for new_state in temp:

                '''
                Calculate expected error of next state:
                '''
                er = new_state.score / (state_to_expand.score + .0001)
                ee = er #er * new_state.score <--- changed this
                #if ee < 0:
                #    ee = new_state.score

                print '\t', new_state.exptree.root.collapse(), "SCORE", new_state.score, "EXPECT: ", ee


                new_score = new_state.score * new_state.depth
                self.states.put((new_score, new_state))

                #new_err = ee + new_state.depth
                #self.states.put((new_err, new_state))




    '''
    Return a score for the fit of exptree on x and y
    '''
    def score(self, exptree, constants):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            a, b = fit.sym_fit(exptree, constants, self.X, self.Y, self.guesses)
            if b < 0:
                return a, float("inf")
            return a, b



'''
---------------------------------------------------------------------------------------------------
'''


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
    plt.show()



'''
---------------------------------------------------------------------------------------------------
'''


def problem_case():
    exptree = ExpTree()
    exptree.apply_binary_op(exptree.root, ops.add)
    l1, l2 = exptree.leaves[0], exptree.leaves[1]
    exptree.apply_unary_op(l1, ops.sin)
    exptree.apply_unary_op(l2, ops.tan)

    x, y = gen_data.get_data(exptree, [])

    print exptree.root.collapse()
    print
    astar = AStar(x, y, False)



    err = np.array([x for x in astar.best_err if not math.isnan(x) and not math.isinf(x)])
    print err
    plt.plot(range(len(err)), err)
    plt.axis([-.1, len(err)+1, -1, max(err)+1])
    plt.show()



'''
---------------------------------------------------------------------------------------------------
'''


def real_data():
    import data


    '''
    Which data to use:
    '''
    y = data.oscillator
    x = [x for x in range(1,len(y)+1)]

    x = [xi/float(max(x)) for xi in x]
    y = [yi/float(max(y)) for yi in y]


    astar = AStar(x, y, 10, 50, False)
    best = astar.min
    besty = gen_data.get_y_data(best.exptree, best.fit_consts, x)


    plt.scatter(x, y)
    plt.hold(True)
    plt.plot(besty)
    plt.show()




def kde():

    import pyqt_fit.kernel_smoothing as smooth

    import data

    '''
    Which data?
    '''
    y = np.array(data.hubbert)
    x = np.array([x for x in range(1,len(y)+1)])

    x = [xi/float(max(x)) for xi in x]
    y = [yi/float(max(y)) for yi in y]

    print "Data:", x, y

    estimator = smooth.SpatialAverage(x, y)
    estimate = estimator.evaluate(x)

    astar = AStar(x, y, .01, 50, False)
    best = astar.min
    besty = gen_data.get_y_data(best.exptree, best.fit_consts, x)


    print "MSE of kernel smoothing estimation: ", mse(y, estimate)
    print "MSE of function-space greedy search: ", mse(y, besty)


    plt.scatter(x, y, color='b')
    plt.hold(True)
    plt.plot(x, estimate, color='g')
    plt.plot(x, besty, color='r')
    plt.show()


def mse(actual, predicted):
    mse = 0
    for i in range(len(actual)):
        diff = predicted[i] - actual[i]
        mse += diff * diff
    return mse


def main():
    kde()
    #real_data()

if __name__ == "__main__":
    main()
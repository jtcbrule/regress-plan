#!/bin/env python3

import operations
import unittest
from exptree import ExpTree
from fit import sse
import numpy as np

class TestSSE(unittest.TestCase):
    def test_sse1(self):
        f = lambda x: x*2
        xd = np.array([1, 2, 3])
        yd = np.array([2, 4, 6])
        self.assertEqual(sse(f, xd, yd), 0)
        
        yd = np.array([2, 3, 3])
        self.assertEqual(sse(f, xd, yd), 10)
        
    def test_sse2(self):
        ''' Make sure we can mix ints and floats '''
        f = lambda x: x*2
        xd = np.array([1])
        yd = np.array([2.5])
        self.assertEqual(sse(f, xd, yd), 0.25)

class TestExpTree(unittest.TestCase):
    def test_deepcopy(self):
        tree = ExpTree()
        tree.apply_binary_op(tree.root, operations.add)
        tree2 = tree.copy()
        self.assertEqual(str(tree), str(tree2))
        
        tree2.apply_binary_op(tree2.root.lhs, operations.mul)
        self.assertNotEqual(str(tree), str(tree2))

if __name__ == "__main__":
    unittest.main()

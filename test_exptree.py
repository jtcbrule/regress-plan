#!/bin/env python3

'''
Unit tests for exptree.py
'''

import operations
import unittest
from exptree import ExpTree

class TestSequenceFunctions(unittest.TestCase):
    def test_deepcopy(self):
        tree = ExpTree()
        tree.apply_binary_op(tree.root, operations.add)
        tree2 = tree.copy()
        self.assertEqual(str(tree), str(tree2))
        
        tree2.apply_binary_op(tree2.root.lhs, operations.mul)
        self.assertNotEqual(str(tree), str(tree2))

if __name__ == "__main__":
    unittest.main()

"""
This class includes different methods for expanding an ExpTree.
"""

import operations as ops

'''
Return a list of new exptrees from expanding exptree
'''
def expand(exptree):

    children = set()

    # 1.) For all leaves:
    for idx in range(len(exptree.leaves)):

        # 2.) For all operations:
        for op in ops.unary_ops:
            temp = exptree.copy()
            temp.apply_unary_op(temp.leaves[idx], op) # Have to index into leaves
            children.add(temp)

        for op in ops.binary_ops:
            temp = exptree.copy()
            temp.apply_binary_op(temp.leaves[idx], op)
            children.add(temp)

        temp = exptree.copy()
        temp.apply_plus_c(temp.leaves[idx])
        children.add(temp)

        temp = exptree.copy()
        temp.apply_times_c(temp.leaves[idx])
        children.add(temp)

    return children


'''
Expands two levels
'''
def expand_two_levels(exptree):

    all_children = set()

    level_1 = expand(exptree)

    for child in level_1:
        all_children.add(child)
        children = expand(exptree)
        for child_child in children:
            all_children.add(child_child)

    return all_children
# Extra Questions
from lab09 import *

# Q5
def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of branches and each pair
    of corresponding branches have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(3, [Tree(2, [Tree(1)])])])
    >>> same_shape(t, s)
    False
    """
    "*** YOUR CODE HERE ***"
    if len(t1.branches) != len(t2.branches):
        return False
    for i in range(0, len(t1.branches)):
        if not same_shape(t1.branches[i], t2.branches[i]):
            return False
    return True 

# Q6
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    # TODO
    def reverse(t, r):
        if r:
            br_len = len(t.branches)
            for i in range(0, br_len // 2):
                t.branches[i].label, t.branches[br_len - i - 1].label = t.branches[br_len - i - 1].label, t.branches[i].label
        for b in t.branches:
            reverse(b, not r)
    reverse(t, True)

# Q7
def next_element(bst, n):
    """
	This function takes in a BST and a number N and it returns the smallest
	element that is greater than N, or None if it has no such element.

    >>> t = BST(8, BST(3, BST(1), BST(6, BST(4), BST(7))), BST(10, BST.empty, BST(14, BST(13))))
    >>> next_element(t, 1)
    3
    >>> next_element(t, 3)
    4
    >>> next_element(t, 5)
    6
    >>> next_element(t, 7)
    8
    >>> next_element(t, 10)
    13
    >>> next_element(t, 14)
    >>> result = [1]
    >>> a = next_element(t, 1)
    >>> while a:
    ...   result += [a]
    ...   a = next_element(t, a)
    >>> result
    [1, 3, 4, 6, 7, 8, 10, 13, 14]
    """
    "*** YOUR CODE HERE ***"
    latest_left_parent = None
    cur = bst
    while cur.label != n:
        if n > cur.label:
            if cur.right is BST.empty:
                break
            cur = cur.right
        elif n < cur.label:
            if cur.left is BST.empty:
                break
            latest_left_parent = cur
            cur = cur.left
    if cur.right is not BST.empty:
        cur = cur.right
        while cur.left is not BST.empty:
            cur = cur.left
        return cur.label
    else:
        if latest_left_parent is None:
            return None
        else:
            return latest_left_parent.label

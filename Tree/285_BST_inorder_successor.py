"""
given a in-order BST root, and a node, return th node's successor'(smallest key greater the node's value)'
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        if p is None:
            return None
        if root != None:

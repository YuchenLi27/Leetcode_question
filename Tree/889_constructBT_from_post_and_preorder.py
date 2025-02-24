"""
given the preorder and postorder traversal of a tree, then to get the tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:

    pre = 0
    post = 0
    def construct(self, preorder, postorder):
        if not preorder or not postorder:
            return []

        root = TreeNode(preorder[self.pre])
        self.pre += 1
        if root.val != postorder[self.post]:
            root.left = self.construct(preorder, postorder)
        if root.val != postorder[self.post]:
            root.right = self.construct(preorder, postorder)
        self.post += 1

        return root




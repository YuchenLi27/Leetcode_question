"""
Question is ask to get the two nodes' LCA
we need to traverse the nodes' parents and the two val has to be the same
we can use recursive to do so
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # remember to check if given nodes are exist
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if we find the p, q in both left and right tree
        # it means this node is the LCA

        if left and right:
            return root
        # otherwise, we'll return the p or q
        return left or right

# time/space: o(n)
# space: because the maximum amount of space utilized by the recursion stack
# would be N since the height of a skewed binary tree could be N.
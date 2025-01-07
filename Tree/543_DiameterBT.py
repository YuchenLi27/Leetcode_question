"""
This question is to find the diameter of a binary tree,
and return the length of the diameter of the tree
we can recursively call the left side tree and right side tree
to do so, we need a helper function, to get the highest subtree

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_longest(node):
            if not node:
                return 0
            nonlocal ans
            # we need to make 'ans' not a local variable
            left = get_longest(node.left)
            right = get_longest(node.right)
            # update the diameter, if the left plus right is longer than the current longest ans.
            ans = max(ans, left + right)
            # it returns the longer one of left and right also plus 1, as we have the root.
            # then we can use the height of left/right to update ans
            return max(left, right) + 1
        # in the out function, we give the root and call helper function.
        ans = 0
        get_longest(root)
        return ans

#time/space: o(n)
# space: during DFS, we call a stack, it depends on the height of the tree.
# for skewed tree: o(n), for balanced tree: o(logN)


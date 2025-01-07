"""
in a BT to find the number of path that the sum of node can be targeted val

"""
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return
            curr_sum += node.val

            if curr_sum == k:
                count += 1

            # The number of times the curr_sum − k has occurred already,
            # determines the number of times a path with sum k
            # has occurred up to the current node
            count += h[curr_sum - k]

            # Add the current sum into a hashmap
            # to use it during the child nodes' processing
            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            # Remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            h[curr_sum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count

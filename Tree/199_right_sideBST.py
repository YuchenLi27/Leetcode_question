"""
Question ask to return the right side of a binary search tree (BST)
from top to bottom
we can handle this question by utilising a queue
this approach allow us to explore each level of the tree before moving to the next one.
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # when there is no root, return an empty list
        if root is None:
            return []

        ans = []
        # we use a deque to store the nodes for level-order traversal
        queue = deque([root])

        while queue:
            n = len(queue)
            # The number of nodes at the current level
            # We iterate through all nodes at the current level
            # for current level, we pop the current node,
            # then we traverse its left and right
            for i in range(n):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                # If we're at the last node of the current level, append its value to ans
                if i == n - 1:
                    ans.append(ele.val)
        return ans
#time/space: o(n)




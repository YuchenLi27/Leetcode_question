"""
BT-Level Traversal
solution1:
1.recursion call, change level and node.left/right
solution2:
1.bfs, deque
"""
from collections import deque


class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
class Solution:
    # solution 1
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.helper(root, 0, [])
        return res

    def helper(self, root, level, res):
        # when len of res is 0, which means we start to put ele into it, and its idx is related to the level.
        level_size = len(res)
        if level_size == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.helper(root.left, level + 1, res)
        if root.right:
            self.helper(root.right, level + 1, res)
    # solution 2
        if not root:
            return []
        res = []
        queue = deque([root])
        level = 0
        while len(queue) != 0:
            res.append([])
            for _ in range(len(queue)):
                root = queue.popleft()
                res[level].append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level += 1
        return res
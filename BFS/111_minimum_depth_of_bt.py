"""
minimun depth: the number of nodes along the shortest path from the root node down to the nearest leaf node
a leaf is a node without children
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = 0
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([root])
        depth = 1
        while len(queue) != 0:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele == None:
                    continue
                elif ele.left == None and ele.right == None:
                    return depth
                else:
                    queue.append(root.left)
                    queue.append(root.right)
            depth += 1
        return -1
"""
similar question 104, which is looking for to get an answer of maximum depth of BT
dfs is a good idea to do so. But for bfs, by using deque() is also possible

"""
class Solution:
    def maxDepth(self, root2):
        if not root2:
            return 0
        queue = deque([root2])
        depth = 0
        while len(queue) != 0:
            depth += 1
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
        return depth

"""
bfs deque
"""
from collections import deque


class Node:
    def __init__(self, children):
        self.val = 0
        self.children = children

class Solution:
    def levelOrder(self, root):
        res = []
        if not root:
            return res

        level = 0
        queue = deque([root])

        while len(queue) != 0:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if level == len(res):
                    res.append([])
                res[level].append(ele.val)
                if ele.children != None:
                    for child in ele.children:
                        queue.append(child)
            level += 1
        return res


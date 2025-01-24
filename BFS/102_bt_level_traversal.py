"""
BT-Level Traversal
solution1:
1.recursion call, change level and node.left/right
solution2:
1.bfs, deque

KEY POINT: when we traverse the bfs, we use deque, the length of deque means the length of the level.
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

"""
traversal in a zigzag level order (leetcode 103)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
solution. 
1: find out which level will be reversed, mark it as true, otherwise mark it as false
2. when finish the round of traversal, make even_level = not even_level to change the status of boolean
3. while it is even level, we need to put the result into the array from right to left, so we just let it pop NOT popleft
4. then we need to pay attention with append ele, current ele is right, so right first, appendleft(ele.right) the left
appendleft(ele.left)

"""
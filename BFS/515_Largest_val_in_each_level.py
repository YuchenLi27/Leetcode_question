"""
515. Find the largest value in each tree row
this question can be answered by using BFS, when we have all nodes from the same level, we can traverse them and
compare its value to get the max value
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def find_largest(root):
        if not root: return []
        ans = []
        queue = deque([root])

        while len(queue) != 0:
            current_nodes = len(queue)
            max_val = float("-inf")
            for node in range(current_nodes):
                node = queue.popleft()
                if node.val >= max_val:
                    max_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_val)
        return ans

# if __name__ == '__main__':
#     root = TreeNode(1)
#     root.left = TreeNode(3)
#     root.right = TreeNode(2)
#     root.left.left = TreeNode(5)
#     root.left.right = TreeNode(3)
#     root.right.right = TreeNode(9)
#     result = TreeNode.find_largest(root)
#     print(result)


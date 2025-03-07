"""
Question ask to validate a binary search tree,
it has to be the left subtree is smaller than the root, and the right subtree is greater than the root
so we can solve this by using recursive or iterative approach
recursive: we need to set the break condition first, no root or smallest.val >= curr.val or largest.val <= curr.val
then have a helper function, keep checking if the condition is right than recursively call the helper function

iterative: DFS is better than BFS, since it faster.
we also can do inorder traversal: left, root, right. get the root.val by using a stack
than move to the left, and pop it
compare it with the prev node to see if is smaller the prev, if so return False, update the prev.val to root.val.
and give the root.right to root
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

"""
class Solution:
    def isValidBST(self, root):
        def bfs(root):
            # we set the min and max value to limit the node
            min_val = float("-inf")
            max_val = float("inf")
            # we store all ele into the queue
            queue = deque([root, min_val, max_val])
            # when there is ele, we pop the node, low, high out to check
            while queue:
                node, low, high = queue.popleft()
                if not low < node.val < high:
                    return False
                # if the ele has left or right subtree, we need to recursive call it
                # and the parameter will be current current_node, low, max

                if node.left:
                    # as it has left side tree, the node will be the max val for that subtree.
                    # ele.left will be current node
                    queue.append([node.left, low, node.val])
                if node.right:
                    # as it has right side tree, the node will be the min val for that subtree.
                    # ele.right will be current node
                    queue.append([node.right, node.val, high])
            return True
        return bfs(root)
# time/space: o(n)
if __name__ == "__main__":
    s = Solution()
    print(s.isValidBST([1, None, 0, 3]))


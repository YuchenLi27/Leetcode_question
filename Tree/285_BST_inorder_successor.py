"""
given a in-order BST root, and a node, return th node's successor'(smallest key greater the node's value)'
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        if p == None or root == None:
            return None

        head = None
        if root != None:
            if p.val > root.val:
                root = root.left
            else:
                head = root
                root = root.right
        return head

if __name__ == "__main__":
    s = Solution()
    print(s.inorderSuccessor([2,1,3], 2))
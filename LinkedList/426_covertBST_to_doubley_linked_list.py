"""
given a BST,the predecessor of the first element is the last element, and the successor of the last element
is the first element. this transformation in place. return the pointer to the smallest element of the linked
list.
"""
class Solution:
    def covertBST(self, root):
        def helper(node):
            nonlocal first, last
            if node != None:
                helper(node.left)
                if last != None:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)

        if root == None:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first


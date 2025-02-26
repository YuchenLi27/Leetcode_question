"""
Question: verify if it is a preorder traversal of a BST
output the boolean value
so we can get the root, and compare the root with the next ele
if next ele is bigger than root, which means the ele will be right/late
otherwise, it will be left/before
"""

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # we assign the min_val to -inf and then compare it with the root
        stack = []
        min_val = float("-inf")

        for i in preorder:
            # if the first ele, which is current root, we can use it to update
            # if the root is smaller than new ele, we update the min_val with the new ele
            # otherwise, we continue this comparison
            while stack and stack[-1] < i:
                min_val = stack.pop()
            if i <= min_val:
                return False
            stack.append(i)
        return True

# time/space: o(n), o(n)
# improve: space o(1)
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = float("-inf")
        i = 0

        for num in preorder:
            while i > 0 and preorder[i - 1] < num:
                min_limit = preorder[i - 1]
                i -= 1

            if num <= min_limit:
                return False

            preorder[i] = num
            i += 1

        return True
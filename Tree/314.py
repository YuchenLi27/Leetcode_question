"""
sort can also sort the negative number in ascending order
this question ask to return the BT in vertical order traversal,
so we can use recursive to call its left and right node and append them into the ans


"""
from collections import deque, defaultdict


# arr = {-2: 1, 3: 2, -1: 0, 0: -3, 2: 4, 5: 3}
# print(sorted(arr.values()))
#
# if __name__ == "__main__":
#     print(sorted(arr.keys()))

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        tb = defaultdict(list)

        while q:
            node, col = q.popleft()
            if node is not None:
                tb[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))

        res = []
        for i in sorted(tb.keys()):
            res.append(tb[i])
        return res


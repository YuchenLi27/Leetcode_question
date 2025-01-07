"""
BST inorder iterator:
left, root, right
pointer to the smallest ele to -1,

"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.idx = -1
        self.inorder(root)
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.nodes.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.idx += 1
        return self.nodes[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.nodes)


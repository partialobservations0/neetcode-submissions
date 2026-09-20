#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            prev_left = root.left if root.left else None
            root.left = root.right if root.right else None
            root.right = prev_left if prev_left else None
            return root

        if not root: return None

        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        invert(root)
        return root

            
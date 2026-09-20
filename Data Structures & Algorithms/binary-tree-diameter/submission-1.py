# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def heightOfTree(root):
            if not root:
                return 0

            return 1 + max(heightOfTree(root.left), heightOfTree(root.right))

        if not root:
            return 0

        lefth = heightOfTree(root.left)
        righth = heightOfTree(root.right)
        dia = lefth + righth
        return max(dia, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

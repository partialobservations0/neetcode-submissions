# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False
        else:

            left_check = (p.left and q.left) or (not p.left and not q.left)
            right_check = (p.right and q.right) or (not p.right and not q.right)
        
            if p.val == q.val and left_check and right_check and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False

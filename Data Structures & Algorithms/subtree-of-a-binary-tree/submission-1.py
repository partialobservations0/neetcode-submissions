# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_subtree(root, subRoot):
            if not root and not subRoot: 
                return True
            if root and subRoot and subRoot.val == root.val:
                if check_subtree(root.left, subRoot.left) and check_subtree(root.right, subRoot.right):
                    return True
                else:
                    return False
            else:
                return False
    
        if not subRoot: return True
        if not root: return False
        
        if check_subtree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




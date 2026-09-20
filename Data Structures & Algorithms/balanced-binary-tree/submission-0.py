# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        # first find height of the binary tree
        def findHeight(root):
            if not root:
                return 0
            
            return 1 + max(findHeight(root.left), findHeight(root.right))
            #if root.left and root.right:
            #    return 1 + max(findHeight(root.left), findHeight(root.right))
            #elif root.left:
            #    return findHeight(root.left)
            #elif root.right:
            #    return findHeight(root.right)
            #else:
            #    return 0
        
        # for each node check left height and right height and their difference
        if not root: 
            return True
        leftheight = findHeight(root.left) #if root.left else 0
        rightheight = findHeight(root.right) #if root.right else 0
        if abs(leftheight - rightheight) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findPath(root, path, node):

            if not root:
                return False
            
            path.append(root)
            if root.val == node.val or findPath(root.left, path, node) or findPath(root.right, path, node):
                return True

            path.pop()
            return False

        ppath = []
        qpath = []
        findPath(root, ppath, p)
        findPath(root, qpath, q)
        
        i = 0
        while i < len(ppath) and i < len(qpath):
            if ppath[i] != qpath[i]:
                return ppath[i-1]
            i += 1
        
        return ppath[i-1]


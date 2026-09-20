# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        self.valsol = [[root.val]]
        def traverse(nodelist):
            if not nodelist:
                return

            sol = []
            tempsol = []
            for node in nodelist:
                if node and node.left: 
                    sol.append(node.left)
                    tempsol.append(node.left.val)
                if node and node.right: 
                    sol.append(node.right)
                    tempsol.append(node.right.val)
            if tempsol:
                self.valsol.append(tempsol)
            if sol: traverse(sol.copy())

        traverse([root])

        return self.valsol

            
    
        
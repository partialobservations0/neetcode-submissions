# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #sol =[]
        # if root.right sol.append(r.r) else sol.append(r.l)
        # check again if r.r.l or r.r.r check again (r.r.child)
        # else check again r.l.child if r.l.child
        self.sol =  [ ]
        def level_traversal(root, level):
            if not root:
                return 

            self.sol.append([])
            self.sol[level].append(root.val)

            level_traversal(root.left,level+1)
            level_traversal(root.right,level+1)
        
        level_traversal(root,0)
        print(self.sol)
        sol2 = []
        for s in self.sol:
            if s:
                sol2.append(s[-1])
        return sol2




    
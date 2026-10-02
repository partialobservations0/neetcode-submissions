class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        curr = []

        def dfs(i, cur):
            if sum(curr) == target:
                sol.append(curr.copy())
                return 
            
            if i >= len(nums) or sum(curr) > target:
                return 
            
            curr.append(nums[i])
            dfs(i, cur)
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0,[])
        return sol

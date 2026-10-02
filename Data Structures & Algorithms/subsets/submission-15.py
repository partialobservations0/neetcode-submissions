class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol = []

        def dfs(i, curr):
            if i >= len(nums):
                if curr not in sol:
                    sol.append(curr.copy())
                return

            curr.append(nums[i])
            if curr not in sol:
                sol.append(curr.copy())
                dfs(i+1,curr)
            curr.pop()
            dfs(i+1, curr)

        dfs(0,[])
        return sol

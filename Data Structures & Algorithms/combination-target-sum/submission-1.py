class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index, cur, total):

            if total == target:
                res.append(cur.copy())
                return 
            
            if index >= len(nums) or total > target: 
                return 

            cur.append(nums[index])
            backtrack(index, cur, total+nums[index])
            cur.pop()
            backtrack(index+1, cur, total)
        
        backtrack(0, [], 0)
        return res
    
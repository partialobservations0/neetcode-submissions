class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # main idea is to find the recursive relationship
        # nums[i] = max(nums[i] + nums[i-2]), nums[i-1]) 
        if len(nums) == 1:
                return nums[0]

        def dp_sol(nums):
            if not nums: 
                return 0 
            if len(nums) == 1:
                return nums[0]

            memo = [0] * len(nums)
            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                memo[i] = max((memo[i-1], memo[i-2] + nums[i]))

            return memo[-1]
        
        return max(dp_sol(nums[1:]), dp_sol(nums[:-1]))
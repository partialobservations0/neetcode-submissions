class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums  - array
        # nums[i] : [2,24,1,4,25,53]
        # [2] - r2
        # [2, 24]  - r24
        # [2, 24, 1] - r24
        # [2,24,1,4] - r24,4
        # [2,24,1,4,25] - r24, 25

        # can i add this number or not 

        if not nums: 
            return 0 

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1] )

        return dp[-1]
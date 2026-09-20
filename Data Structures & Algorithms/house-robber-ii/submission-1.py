class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def mysol(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[1],nums[0])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
                print("in dp")
            return dp[-1]

        s1 = mysol(nums[0:-1])
        s2 = mysol(nums[1:])
        print(s1)
        print(s2)
        return max(s1,s2)
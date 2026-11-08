class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMax, curMin = 1, 1
        for num in nums: 
            tmp = curMax * num
            curMax = max(tmp, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res

        res = nums[0]
        
        for i, n in enumerate(nums):
            curr = n
            res = max(res, curr)
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)

        return res


        n = len(nums)
        prod = [[-1*float('inf') for _ in range(n)] for _ in range(n)]
        for i,num in enumerate(nums):
            prod[i][i] = num
        maxval = max(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                prod[i][j] = prod[i][j-1] * nums[j]
                if prod[i][j] > maxval:
                    maxval = prod[i][j]
        return maxval

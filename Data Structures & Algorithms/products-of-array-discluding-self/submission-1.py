class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = 0
        for i in nums:
            if i == 0:
                zerocount += 1
            else:
                prod = prod*i
        res = [0]*len(nums)
        if zerocount > 1:
            return res
        if zerocount == 1:
            i = nums.index(0)
            res[i] = prod
            return res
        else:
            for i,n in enumerate(nums):
                res[i] = int(prod/n)
            return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over the entire array two times find two numbers that sum up to target
        # better: replace one iteration with hash storage
        # store numbers in a hash
        numsHashed = {}
        for i,n in enumerate(nums):
            numsHashed[n] = i
        for i,n in enumerate(nums):
            if target - n in numsHashed:
                if i != numsHashed[target-n]:
                    return [i,numsHashed[target - n]]
        return [0,0]

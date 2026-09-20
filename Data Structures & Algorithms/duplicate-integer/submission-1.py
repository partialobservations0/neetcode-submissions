class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = {}
        for index,num in enumerate(nums):
            if num in alreadySeen.keys():
                return True
            else:
                alreadySeen[num] = 1
        return False

        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        """mydict = {}
        for i,n in enumerate(nums):
            if n in mydict:
                return True
            else:
                mydict[n] = 1
        return False"""

        return (len(nums) != len(set(nums)))

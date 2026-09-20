class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.sol = [ [] ]
        def traverse(nums):
            if nums in self.sol:
                return 
            if len(nums) == 1:
                if nums not in self.sol:
                    self.sol.append(nums)
                return
            if nums not in self.sol:
                self.sol.append(nums)
            for i in range(0,len(nums)):
                traverse( nums[:i] + nums[i+1:])
        traverse(nums)
        return self.sol



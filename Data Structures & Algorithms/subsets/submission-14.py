class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def backtrack(index):
            if len(nums) <= index:
                res.append(curr.copy())
                return
            
            curr.append(nums[index])
            backtrack(index+1)
            curr.pop()
            backtrack(index+1)

        backtrack(0)
        return res



        """
        res = []
        curr = []
        def backtrack(index):
            if index >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            backtrack(index+1)
            curr.pop()
            backtrack(index+1)
        
        backtrack(0)
        return res
        """


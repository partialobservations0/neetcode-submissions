class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        subset = []

        def backtrack(index,subset):

            if index >= len(nums) :
                res.add(tuple(subset.copy()))
                return 
            
            subset.append(nums[index])
            backtrack(index+1, subset)
            subset.pop()
            backtrack(index+1,subset)
        
        nums.sort()
        backtrack(0,[])
        return [list(s) for s in res]
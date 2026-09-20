class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # lets repeat the question out loud
        # give array of integers containing n+1 integers : does that mean length of array is n+1 or 
        # that there are n+1 integers? Each number is in range [1,n]
        # example: [1, 2, 4, 3, 5, 5]
        # if its sorted then one pass find repeat entry: if arr[n+1] == arr[n]; sort and then one pass
        # hash map : take length n, one pass over integers, map[arr[n]] = True; if map[arr[n]] == True 
        # lets try brute force first
        # only integers: Do integers have range? : must be
        # how long can the array be?
        # is it sorted?

        if not nums:
            return -1

        seen = {}
        for i,n in enumerate(nums):
            if n in seen:
                return n
            else:
                seen[n] = True
        return -1
        
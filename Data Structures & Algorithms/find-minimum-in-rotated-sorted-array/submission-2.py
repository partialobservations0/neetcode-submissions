class Solution:
    def findMin(self, nums: List[int]) -> int:
        # solution is binary tree search
        # lets say the array was not rotated 
        # pseudocode for binary search
        # return the minimum element
        
        # we do a binary search, where we first identfy the left and right
        # index to search withing and then call the function recursively

        leftindex = 0
        rightindex = len(nums) - 1
        mid = (leftindex + rightindex) // 2

        # to make sure that left:mid and mid+1 to right is sorted
        # to check if it sorted compare mid and left for left array
        # and compare right and mid+1 for right array

        # for the one that is sorted the min is left is the minimum
        # for not sorted one call the function again and find the minimum of minimums
        
        #curr_min = 1000
        if len(nums) == 1:
            return nums[0]

        # to check sorted 
        if nums[mid] > nums[leftindex]:
            min_left = nums[leftindex]
        else:
            min_left = self.findMin(nums[leftindex:mid+1])
        
        if nums[rightindex] > nums[mid + 1]:
            min_right = nums[mid+1]
        else:
            min_right = self.findMin(nums[mid+1:rightindex+1])
        
        return min(min_left, min_right)

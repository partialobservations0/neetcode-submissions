class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,left,right):
            if right < left: 
                return - 1
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binary(nums, left, mid - 1)
            elif target > nums[mid]:
                return binary(nums, mid + 1, right)
            else:
                return -1 
        return binary(nums, 0, len(nums)-1)

            
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums,left,right):
            if not nums: return -1
            if left > right: return -1
            
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(nums, left, mid - 1)
            elif nums[mid] < target:
                return binary(nums, mid+1, right)
            else:
                return -1
        return binary(nums,0,len(nums)-1)
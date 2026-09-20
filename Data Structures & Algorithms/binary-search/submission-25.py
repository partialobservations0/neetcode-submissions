class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums):
            left = 0
            right = len(nums)
            
            while right > left:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid 
            return -1

        def binary_rec(nums, left=0, right=len(nums)):
            if not nums:
                return -1
            if right - left == 1:
                if nums[left] == target:
                    return left
                else:
                    return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                binary_rec(nums,mid+1,right)
            elif nums[mid] > target:
                binary_rec(nums,left,mid)
            
        return binary(nums)

            
            
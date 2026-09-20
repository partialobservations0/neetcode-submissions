class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftindex = 0 
        rightindex = len(nums) - 1
        mid = int((leftindex + rightindex) / 2)

        # we know if the left sided array is sorted if 
        # nums[mid] > nums[left] and if target is less than nums[mid]
        # it is in this array

        if len(nums) == 1 :
            if nums[0] == target:
                return 0
            else:
                return -1

        while leftindex < rightindex:
            mid = int((leftindex + rightindex) / 2)

            if target == nums[mid]:
                return mid
            if target == nums[leftindex]:
                return leftindex
            if target == nums[rightindex]:
                return rightindex

            print(leftindex)
            print(rightindex)
            print(mid)

            if nums[mid] >= nums[leftindex]:
                if nums[mid] >= target and nums[leftindex] <= target:
                    rightindex = mid
                else:
                    leftindex = mid+1
            else:
                if nums[mid] < target and nums[rightindex] > target:
                    leftindex = mid + 1
                else:
                    rightindex = mid

        return -1 

        # else:
            # target in rotated array so continue

                
